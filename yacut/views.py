from flask import flash, redirect, render_template

from . import app
from .constants import NAME_ALREADY_USE_ERROR_VIEWS
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    if URLMap.get(short=form.custom_id.data).first():
        flash(NAME_ALREADY_USE_ERROR_VIEWS.format(name=form.custom_id.data))
        return render_template('index.html', form=form)
    return render_template(
        'index.html',
        form=form,
        url=URLMap.create_url(
            original=form.original_link.data,
            short=form.custom_id.data or URLMap.get_unique_short_id(),
        ),
    )


@app.route('/<short>', methods=['GET'])
def redirect_view(short):
    return redirect(
        URLMap.get(short=short).first_or_404().original
    )
