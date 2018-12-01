from flask import flash, redirect, url_for, session, render_template
from app import app
from .forms import QuoteForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = QuoteForm()

    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
