# YACUT
# Укоротитель ссылок

### Тенологии используемые в проекте:
- python 3.8
- flask 2.0.2
- jinja2 3.0.3
- sqlalchemy 1.4.29

### Пример работы:
на главной странице в поле "Длинная ссылка" вставляем ссылку которую хотим укоротить:
```
https://yandex.ru/search/?text=github&lr=240&clid=2270456&search_source=yaru_desktop_common&src=suggest_B
```
Получаем:
```
http://127.0.0.1:5000/f7wgGQ
```

### Как запустить проект:
Клонировать репозиторий:
```
git clone https://github.com/russ044/yacut.git
```
Создать и активировать виртуальное окружениеи:
```
python -m venv venv
.\venv\Scripts\activate
```
Установить зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции и запустить:
```
flask db init
flask db migrate
flask db upgrade
flask run
```

## [Cпецификации API](https://github.com/russ044/yacut/blob/master/openapi.yml)
Доступные endpoints:
```
/api/id/
/api/id/{short_id}/
```

Создание короткой ссылки:
```
Запрос: POST  /api/id/
Тело запроса:
{
    "url": "string",
    "custom_id": "string",
}
```

Получение полного URL по короткой ссылке:
```
Запрос: GET  /api/id/{short_id}/
```



### Автор проекта:
- Емцов А.В.  [russ044](https://github.com/russ044)
