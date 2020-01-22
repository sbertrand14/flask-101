# tests/test_views.py
from flask_testing import TestCase
from flask import jsonify
from wsgi import app, PRODUCTS

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertEquals(len(products), len(PRODUCTS)) # 2 is not a mistake here.

    def test_one_product_json(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assert200(response)
        self.assertEquals(product["id"],1)
        self.assertEquals(product["name"],"Skello")

    def test_no_product_json(self):
        response = self.client.get("/api/v1/products/0")
        self.assert404(response)

    def test_delete_product(self):
        response = self.client.get("/api/v1/products/3")
        product = response.json
        self.assert200(response)

        response = self.client.delete("/api/v1/products/3")
        self.assert_status(response,204)

        response = self.client.delete("/api/v1/products/3")
        self.assert404(response)

        response = self.client.get("/api/v1/products/3")
        product = response.json
        self.assert404(response)

    def test_create_product(self):
        newproduct = { 'id': 0, 'name': 'newproduct' }
        response = self.client.post("/api/v1/products", json=newproduct)
        productreturned = response.get_json()
        self.assert_status(response,201)
        self.assertIsInstance(productreturned, dict)
        self.assertEquals(productreturned["id"], len(PRODUCTS))
