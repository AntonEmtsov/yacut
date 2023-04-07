from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import CustomErrorModels, InvalidAPIUsage
from .models import URLMap

ID_NOT_FOUND_ERROR = 'Указанный id не найден'
REQUEST_MISSING_ERROR = 'Отсутствует тело запроса'
URL_REQUIRED_FIELD_ERROR = '"url" является обязательным полем!'


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    short = URLMap.get(short=short_id)
    if not short:
        raise InvalidAPIUsage(ID_NOT_FOUND_ERROR, 404)
    return jsonify({'url': short.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(REQUEST_MISSING_ERROR)
    if 'url' not in data or not data['url']:
        raise InvalidAPIUsage(URL_REQUIRED_FIELD_ERROR)
    try:
        return jsonify(URLMap.create(
            data['url'],
            data.get('custom_id'),
            True,
        ).to_dict()), HTTPStatus.CREATED
    except (CustomErrorModels, ValueError) as error:
        raise InvalidAPIUsage(error.message)
