from flask import flash, redirect, url_for, session, render_template
from app import app
from app import model, tokenize,graph
from tensorflow import keras
from .forms import QuoteForm
from keras import backend as K

class Prediction:
    def __init__(self, quote, probability):
        self.quote = quote
        prob = probability[0][0]
        if(float(prob) > 0.5):
            print("is shakespeare")
            self.isShakespeare = True
            self.probability = prob*100

        else:
            self.isShakespeare = False
            self.probability = (1-prob)*100


@app.route('/', methods=['GET', 'POST'])
def index():
    form = QuoteForm()

    if form.validate_on_submit():
        response = predict(form.quote.data)
        return render_template('index.html', form=form, response=response)
    return render_template('index.html', form=form, response=None)

@app.route('/predict')
def predict(string):
    quote = tokenize.texts_to_sequences([string])
    quote = keras.preprocessing.sequence.pad_sequences(quote, value=0,
                                                        padding='post',
                                                        maxlen=20)
    with graph.as_default():
        probability = model.predict(quote,verbose=1)

    return Prediction(string, probability)
