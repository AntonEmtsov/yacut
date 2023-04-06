import random
from datetime import datetime

from flask import url_for

from settings import (FIELD_LENGHT_ORIGINAL, FIELD_LENGHT_SHORT,
                      NUMBER_LINK_GENERATION, NUMBER_SYMBOLS)

from . import db
from .constants import SYMBOLS
from .error_handlers import InvalidAPIUsage

ID_NOT_FOUND_ERROR = 'Указанный id не найден'
INVALID_NAME_ERROR = 'Указано недопустимое имя для короткой ссылки'
NAME_ALREADY_USE_ERROR = 'Имя "{name}" уже занято.'
NAME_ALREADY_USE_ERROR_VIEWS = 'Имя {name} уже занято!'
REQUEST_MISSING_ERROR = 'Отсутствует тело запроса'
REQUIRED_FIELD_ERROR = 'Обязательное поле'
SYMBOLS_ERROR = 'Только буквы и цифры'
URL_REQUIRED_FIELD_ERROR = '"url" является обязательным полем!'
FAILED_GENERATE_LINK = 'Не удалось сгенерировать ссылку'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(FIELD_LENGHT_ORIGINAL), nullable=False)
    short = db.Column(
        db.String(FIELD_LENGHT_SHORT),
        unique=True,
        nullable=False,
    )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view',
                short=self.short,
                _external=True,
            )
        )

    @staticmethod
    def get_unique_short_id():
        for _ in range(NUMBER_LINK_GENERATION):
            short_id = ''.join(random.choices(SYMBOLS, k=NUMBER_SYMBOLS))
            if not URLMap.get(short=short_id).first():
                return short_id
        raise InvalidAPIUsage('Не удалось сгенерировать ссылку')

    @staticmethod
    def get(**kwargs):
        return URLMap.query.filter_by(**kwargs)

    @staticmethod
    def create_url(original, short):
        if not short:
            short = URLMap.get_unique_short_id()
        url = URLMap(original=original, short=short)
        db.session.add(url)
        db.session.commit()
        return url

    @staticmethod
    def validate_short(custom_id):
        if len(custom_id) > 16:
            raise InvalidAPIUsage(INVALID_NAME_ERROR)
        if set(custom_id).difference(SYMBOLS):
            raise InvalidAPIUsage(INVALID_NAME_ERROR)
        if URLMap.get(short=custom_id).first():
            raise InvalidAPIUsage(
                NAME_ALREADY_USE_ERROR.format(name=custom_id)
            )
        return custom_id
