from flask import Flask, render_template, request

#render template allows us to pull in html file template 

app = Flask(__name__) #create instance of flask web application 

#making web pages and defining how to access the page
@app.route("/", methods=["GET"]) #defining path to get to the function
def home():
    return render_template("index.html") #referencing the html page 

@app.route('/', methods=['POST'])
def predict():
    image = load_img(image_path, target_size=(224,224))
    image = img_to_array(image)
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = decode_predictions(yhat)
    label=label[0][0]

    classification ='%s (%.2f%%)' % (label[1],label[2]*100)

    return render_template('index.html', prediction=classification)


#now running the app
if __name__ == "__main__":
    app.run(port =3000, debug=True)
