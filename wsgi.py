# wsgi.py
from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'truc' }
]


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
    newproduct = request.get_json()
    newproduct["id"] = ID.next()
    PRODUCTS.append(newproduct)
    return make_response(jsonify(newproduct),201)
