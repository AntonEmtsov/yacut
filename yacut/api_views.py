from http import HTTPStatus

from flask import jsonify, request

from . import app
from .constants import (ID_NOT_FOUND_ERROR, REQUEST_MISSING_ERROR,
                        URL_REQUIRED_FIELD_ERROR)
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    short = URLMap.get(short=short_id).first()
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
    # custom_id = 'custom_id'
    if 'custom_id' not in data or not data['custom_id']:
        short = URLMap.get_unique_short_id()
    else:
        short = URLMap.validate_short(data['custom_id'])
    return jsonify(
        URLMap.create_url(original=data['url'], short=short).to_dict()
    ), HTTPStatus.CREATED
