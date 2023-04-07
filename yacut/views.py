from flask import abort, flash, redirect, render_template

from . import app
from .error_handlers import CustomErrorModels
from .forms import URLForm
from .models import URLMap

NAME_ALREADY_USE_ERROR_VIEWS = 'Имя {name} уже занято!'


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        url_map = URLMap.create(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        return render_template(
            'index.html',
            form=form,
            short_link=url_map.get_short_url(),
        )
    except CustomErrorModels as error:
        flash(error.message)
        return render_template('index.html', form=form)


@app.route('/<short>', methods=['GET'])
def redirect_view(short):
    short_link = URLMap.get(short=short)
    if short_link:
        return redirect(short_link.original)
    abort(404)
