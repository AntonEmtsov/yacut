from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from settings import FIELD_LENGHT_ORIGINAL, FIELD_LENGHT_SHORT, REGEX

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
            Length(max=FIELD_LENGHT_ORIGINAL),
        ])
    custom_id = StringField(
        SHORT_LINK,
        validators=[
            Length(max=FIELD_LENGHT_SHORT),
            Optional(),
            Regexp(REGEX, message=SYMBOLS_ERROR),
        ]
    )
    submit = SubmitField(CREATE)
