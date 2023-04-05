from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import (ID_NOT_FOUND_ERROR, INVALID_NAME_ERROR,
                        NAME_ALREADY_USE_ERROR, REQUEST_MISSING_ERROR, SYMBOLS,
                        URL_REQUIRED_FIELD_ERROR)
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .random_string import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage(ID_NOT_FOUND_ERROR, 404)
    return jsonify({'url': url.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(REQUEST_MISSING_ERROR)
    if 'url' not in data or not data['url']:
        raise InvalidAPIUsage(URL_REQUIRED_FIELD_ERROR)
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id()
    if 'custom_id' in data:
        if len(data['custom_id']) > 16:
            raise InvalidAPIUsage(INVALID_NAME_ERROR)
        if set(data['custom_id']).difference(SYMBOLS):
            raise InvalidAPIUsage(INVALID_NAME_ERROR)
        if URLMap.query.filter_by(short=data['custom_id']).first():
            raise InvalidAPIUsage(
                NAME_ALREADY_USE_ERROR.format(name=data['custom_id'])
            )
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED
