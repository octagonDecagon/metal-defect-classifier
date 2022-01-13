from flask import Flask, render_template, request


#render template allows us to pull in html file template 

backend = Flask(__name__) #create instance of flask web application 

#making web pages and defining how to access the page
@backend.route("/", methods=["GET"]) #defining path to get to the function
def home():
    return render_template("index.html") #referencing the html page 

@backend.route("/aboutus.html", methods=["GET"])
def aboutus():
    return render_template("aboutus.html")

@backend.route("/index.html", methods=["GET"])
def backhome():
   return render_template("index.html")

@backend.route("/defects.html", methods=["GET"])
def defects():
   return render_template("defects.html")

@backend.route('/', methods=['POST'])
def predict():
    image = load_img(image_path, target_size=(224,224))
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


