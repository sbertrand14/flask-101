# wsgi.py
from flask import Flask, jsonify, abort
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'truc' }
]

@app.route('/api/v1/products')
def get_products():
    return jsonify(PRODUCTS)

@app.route('/api/v1/products/<int:id>')
def get_product(id):
    for x in PRODUCTS:
        if x["id"] == id:
            return jsonify(x)
    abort(404)
