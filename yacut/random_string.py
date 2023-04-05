import random

from .constants import SYMBOLS
from .models import URLMap


def get_unique_short_id():
    while True:
        result = ''.join(random.choices(SYMBOLS, k=6))
        if URLMap.query.filter_by(short=result).first():
            continue
        return result
