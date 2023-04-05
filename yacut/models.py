from datetime import datetime

from flask import url_for

from . import db

FIELDS = {
    'original': 'url',
    'short': 'custom_id',
}


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(2048), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_view',
                short=self.short,
                _external=True,
            )
        )

    def from_dict(self, data):
        for key, value in FIELDS.items():
            if value in data:
                setattr(self, key, data[value])
