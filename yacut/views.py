from flask import flash, redirect, render_template

from . import app, db
from .constants import NAME_ALREADY_USE_ERROR_VIEWS
from .forms import URLForm
from .models import URLMap
from .random_string import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    if URLMap.query.filter_by(short=form.custom_id.data).first():
        flash(NAME_ALREADY_USE_ERROR_VIEWS.format(name=form.custom_id.data))
        return render_template('index.html', form=form)
    url = URLMap(
        original=form.original_link.data,
        short=form.custom_id.data or get_unique_short_id(),
    )
    db.session.add(url)
    db.session.commit()
    return render_template('index.html', form=form, url=url)


@app.route('/<short>', methods=['GET'])
def redirect_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
