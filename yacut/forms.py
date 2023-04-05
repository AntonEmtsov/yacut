from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import REGEX, REQUIRED_FIELD_ERROR, SYMBOLS_ERROR


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message=REQUIRED_FIELD_ERROR),
            Length(1, 2048),
        ])
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(REGEX, message=SYMBOLS_ERROR),
        ]
    )
    submit = SubmitField('Создать')
