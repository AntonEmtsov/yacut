# YACUT
# Укоротитель ссылок

### Тенологии используемые в проекте:
- python 3.8
- flask 2.0.2
- jinja2 3.0.3
- sqlalchemy 1.4.29

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
Запустить:
```
flask run
```
### Пример работы:
на главной странице в поле "Длинная ссылка" вставляем ссылку которую хотим укоротить:
```
https://yandex.ru/search/?text=github&lr=240&clid=2270456&search_source=yaru_desktop_common&src=suggest_B
```
Получаем:
```
http://127.0.0.1:5000/f7wgGQ
```

### Автор проекта:
- Емцов А.В.  [russ044](https://github.com/russ044)
