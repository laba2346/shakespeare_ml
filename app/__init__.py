from flask import Flask
from keras.models import load_model, model_from_json
from keras import backend as K
import tensorflow as tf

import pickle

app = Flask(__name__, instance_relative_config=True)

from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform

model = load_model('shake_model.h5')
graph = tf.get_default_graph()



with open('tokenize.pickle', 'rb') as handle:
    tokenize = pickle.load(handle)

from app import routes

app.config.from_object('config')
