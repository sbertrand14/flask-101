# wsgi.py
from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

INITIAL_PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'truc' }
]

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'truc' }
]

from copy import copy
def reset_products():
    PRODUCTS = copy(INITIAL_PRODUCTS)

class Counter:
    def __init__(self):
        self.id = 3

    def next(self):
        self.id += 1
        return self.id

ID = Counter()

@app.route('/api/v1/products')
def get_products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>')
def get_product(id):
    for x in PRODUCTS:
        if x["id"] == id:
            return make_response(jsonify(x), 200)
    abort(404)

@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def del_product(id):
    for x in PRODUCTS:
        if x["id"] == id:
            PRODUCTS.remove(x)
            return make_response("", 204)
    abort(404)

@app.route('/api/v1/products', methods=['POST'])
def add_product():
    requestedproduct = request.get_json()
    newproduct = {"id": ID.next(), "name": requestedproduct["name"]}
    PRODUCTS.append(newproduct)
    return make_response(jsonify(newproduct),201)


@app.route('/api/v1/products/<int:id>', methods=['PATCH'])
def update_product(id):
    requestedproduct = request.get_json()
    if requestedproduct["name"] == "":
        abort(422)

    for x in PRODUCTS:
        if x["id"] == id:
            x["name"] = requestedproduct["name"]
            return make_response("", 204)

    abort(404)
