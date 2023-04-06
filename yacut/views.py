from flask import flash, redirect, render_template

from . import app
from .forms import URLForm
from .models import URLMap

NAME_ALREADY_USE_ERROR_VIEWS = 'Имя {name} уже занято!'


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short = form.custom_id.data
    if URLMap.get(short=short).first():
        flash(NAME_ALREADY_USE_ERROR_VIEWS.format(name=short))
        return render_template('index.html', form=form)
    if not short:
        short = URLMap.get_unique_short_id()
    return render_template(
        'index.html',
        form=form,
        short_link=URLMap.create_url(
            original=form.original_link.data,
            short=short
        ).get_short_url(),
    )


@app.route('/<short>', methods=['GET'])
def redirect_view(short):
    return redirect(
        URLMap.get(short=short).first_or_404().original
    )
