from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from settings import (MAX_LENGHT_ORIGINAL_LINK, MAX_LENGHT_SHORT_LINK,
                      REGEX_SHORT_LINK)

CREATE = 'Создать'
ORIGINAL_LINK = 'Длинная ссылка'
REQUIRED_FIELD_ERROR = 'Обязательное поле'
SHORT_LINK = 'Ваш вариант короткой ссылки'
SYMBOLS_ERROR = 'Только буквы и цифры'


class URLForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LINK,
        validators=[
            DataRequired(message=REQUIRED_FIELD_ERROR),
            Length(max=MAX_LENGHT_ORIGINAL_LINK),
        ])
    custom_id = StringField(
        SHORT_LINK,
        validators=[
            Length(max=MAX_LENGHT_SHORT_LINK),
            Optional(),
            Regexp(REGEX_SHORT_LINK, message=SYMBOLS_ERROR),
        ]
    )
    submit = SubmitField(CREATE)
