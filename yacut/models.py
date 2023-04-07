import random
from datetime import datetime

from flask import url_for

from settings import (MAX_LENGHT_ORIGINAL_LINK, MAX_LENGHT_SHORT_LINK,
                      NUMBER_LINK_GENERATION, NUMBER_RANDOM_SYMBOLS_SHORT_LINK,
                      REDIRECT_VIEW_NAME, REGEX_SHORT_LINK,
                      VALID_SYMBOLS_SHORT_LINK)

from . import db
from .error_handlers import InvalidUsage

FAILED_GENERATE_LINK = 'Не удалось сгенерировать ссылку!'
INVALID_NAME_ERROR = 'Указано недопустимое имя для короткой ссылки'
NAME_ALREADY_USE_ERROR = 'Имя "{name}" уже занято.'
NAME_ALREADY_USE_ERROR_VIEWS = 'Имя {name} уже занято!'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LENGHT_ORIGINAL_LINK), nullable=False)
    short = db.Column(
        db.String(MAX_LENGHT_SHORT_LINK),
        unique=True,
        nullable=False,
    )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=self.get_short_url()
        )

    def get_short_url(self):
        return url_for(REDIRECT_VIEW_NAME, short=self.short, _external=True)

    @staticmethod
    def get_unique_short_id():
        for _ in range(NUMBER_LINK_GENERATION):
            short_id = ''.join(random.choices(
                VALID_SYMBOLS_SHORT_LINK,
                k=NUMBER_RANDOM_SYMBOLS_SHORT_LINK,
            ))
            if not URLMap.get(short=short_id):
                return short_id
        raise InvalidUsage(FAILED_GENERATE_LINK)

    @staticmethod
    def get(**kwargs):
        return URLMap.query.filter_by(**kwargs).first()

    @staticmethod
    def create_url_map(original, short=None, flag=True):
        if not short:
            short = URLMap.get_unique_short_id()
        elif len(short) > MAX_LENGHT_SHORT_LINK:
            raise InvalidUsage(INVALID_NAME_ERROR)
        elif set(short).difference(REGEX_SHORT_LINK):
            raise InvalidUsage(INVALID_NAME_ERROR)
        elif URLMap.get(short=short):
            raise InvalidUsage(
                NAME_ALREADY_USE_ERROR.format(name=short) if flag else
                NAME_ALREADY_USE_ERROR_VIEWS.format(name=short)
            )
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
