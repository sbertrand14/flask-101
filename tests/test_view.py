# tests/test_views.py
from flask_testing import TestCase
from flask import request
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.


    def test_one_product_json(self):
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assert200(response)
        print(product)
        self.assertEquals(product["id"],1)
        self.assertEquals(product["name"],"Skello")

    def test_no_product_json(self):
        response = self.client.get("/api/v1/products/0")
        self.assert404(response)

    # def test_delete_product(self):
    #     response = self.client.delete("/api/v1/products/1")
    #     self.assert_status(response,204)

    # def test_create_product(self):
    #     response = self.client.post("/api/v1/products")

    #     self.assert_status(response,204)
