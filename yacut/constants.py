from string import ascii_letters, digits

REGEX = '^[a-zA-Z0-9]+$'
SYMBOLS = ascii_letters + digits

# Фразы ошибок
ID_NOT_FOUND_ERROR = 'Указанный id не найден'
INVALID_NAME_ERROR = 'Указано недопустимое имя для короткой ссылки'
NAME_ALREADY_USE_ERROR = 'Имя "{name}" уже занято.'
NAME_ALREADY_USE_ERROR_VIEWS = 'Имя {name} уже занято!'
REQUEST_MISSING_ERROR = 'Отсутствует тело запроса'
REQUIRED_FIELD_ERROR = 'Обязательное поле'
SYMBOLS_ERROR = 'Только буквы и цифры'
URL_REQUIRED_FIELD_ERROR = '"url" является обязательным полем!'
