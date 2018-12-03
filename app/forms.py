from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField
from wtforms.validators import DataRequired

class QuoteForm(FlaskForm):
    quote = StringField('quote', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):
        filled = FlaskForm.validate(self)

        if not filled:
            return False
        quote = self.quote.data
        numWords = len(quote.split(' '))

        if(numWords < 10):
            self.quote.errors.append('Too few words. Please input at least 10 words and at most 20')
            return False
        elif(numWords > 20):
            self.quote.errors.append("Too many words. Please input at most 20 words and at least 10")
            return False
        else:
            return True
