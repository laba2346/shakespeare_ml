from flask import flash, redirect, url_for, session, render_template
from app import app
from app import model, tokenize,graph
from tensorflow import keras
from .forms import QuoteForm
from keras import backend as K



@app.route('/', methods=['GET', 'POST'])
def index():
    form = QuoteForm()

    if form.validate_on_submit():
        predict(form.quote.data)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/predict')
def predict(string):
    quote = tokenize.texts_to_sequences([string])
    quote = keras.preprocessing.sequence.pad_sequences(quote, value=0,
                                                        padding='post',
                                                        maxlen=20)
    with graph.as_default():
        flash(str(model.predict(quote,verbose=1)))
