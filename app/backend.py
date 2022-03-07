from flask import Flask, render_template, request, jsonify
import base64
import io
from PIL import Image
import keras
from keras. models import Sequential
from keras. models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
from tensorflow import keras
import tensorflow as tf
import sys
import numpy as np

#import model 
#global model
#model = tf.keras.models.load_model("resnet50_weights_tf_dim_ordering_tf_kernels.h5")
#print("* Model loaded!")

#render template allows us to pull in html file template

backend = Flask(__name__) #create instance of flask web application

#making web pages and defining how to access the page
@backend.route("/", methods=["GET"]) #defining path to get to the function
def home():
    return render_template("index.html") #referencing the html page

@backend.route("/index.html", methods=["GET"]) #defining path to get to the function
def index():
    return render_template("index.html") #referencing the html page

@backend.route("/aboutus.html", methods=["GET"])
def aboutus():
    return render_template("aboutus.html")

@backend.route("/index.html", methods=["GET"])
def backhome():
   return render_template("index.html")

@backend.route("/defects.html", methods=["GET"])
def defect():
   return render_template("defects.html")

@backend.route('/defects.html', methods=['POST']) #creating post request for user upload 
def predict(): #creating prediction function
    imagefile = request.files['imagefile']; #name from defects.html
    image_path ="./images/" +imagefile.filename;
    imagefile.save(image_path); #creatig ability to save image 

    #now want to load model and pass image into the renderer

    #image = load_img(images_path, target_size=(224,224);
    image = img_to_array(image)
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = decode_predictions(yhat)
    label=label[0][0]

    classification ='%s (%.2f%%)' % (label[1],label[2]*100)

    return render_template('defects.html', prediction=classification)


#now running the app
if __name__ == "__main__":
    backend.run(port =3000, debug=True)
