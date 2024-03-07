from flask import Flask #inside the flask framework use the Flask library

app = Flask(__name__) #__name__ this is using the name of the folder i.e. 107

@app.get("/")
def home():
    return "Hello from flask"

app.run(debug=True) #this applies the changes on the code live