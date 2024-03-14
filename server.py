from flask import Flask, request, jsonify #inside the flask framework use the Flask library
import json


app = Flask(__name__) # __name__ this is using the name of the folder i.e. 107

#initialize the products as an empty list
products = [] 

# Welcome message
@app.get("/")
def home():
    return "Welcome home"
# GET /api/catalog

# this time we need to read and write in to the server
@app.get("/api/products")
def get_products():
    global products
    if not products:
        products = [
            {"id": 1, "name": "Product 1", "price": 10.99},
            {"id": 2, "name": "Product 2", "price": 19.99},
        ]
    return jsonify(products)

@app.post("/api/products")
def save_products():
    # should save a new product
    product = request.get_json() 
    print(product)
    # mock the save
    products.append(product)
    return jsonify({"message": "product successfully added", "product": product}), 201


@app.get("/testing")
def test():
    return "hello from another page"

# create 2 more API's (about and blog)

@app.get("/about")
def about():
    me = {"name":"Andrew"}
    return jsonify(me)

@app.get("/blog")
def blog():
    return "blog"

@app.route("/version")
def version():
    version = {"name":"mouse","version":"2","build":12346}
    return jsonify(version)

if __name__ == "__main__":
    app.run(debug=True) # this applies the changes on the code live