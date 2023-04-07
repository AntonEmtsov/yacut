import os
import re
from string import ascii_letters, digits

MAX_LENGHT_ORIGINAL_LINK = 2048
MAX_LENGHT_SHORT_LINK = 16
NUMBER_LINK_GENERATION = 5
NUMBER_RANDOM_SYMBOLS_SHORT_LINK = 6

VALID_SYMBOLS_SHORT_LINK = ascii_letters + digits
REGEX_SHORT_LINK = fr'[{re.escape(str(VALID_SYMBOLS_SHORT_LINK))}]'
REDIRECT_VIEW_NAME = 'redirect_view'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        default='sqlite:///db.sqlite3',
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
