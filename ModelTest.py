import os
import numpy as np
import tensorflow as tf
from tensorflow import keras

#Need Example Dataset
model = tf.keras.models.load_model("model90acc.h5")
model.predict()