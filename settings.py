import os

FIELD_LENGHT_ORIGINAL = 2048
FIELD_LENGHT_SHORT = 16
NUMBER_LINK_GENERATION = 500
NUMBER_SYMBOLS = 6

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI',
        default='sqlite:///db.sqlite3',
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
