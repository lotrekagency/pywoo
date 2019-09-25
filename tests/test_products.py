import unittest

from mock import patch

from pywoo.models.product_categories import ProductCategory
from pywoo.pywoo import Api
from pywoo.models.products import Product
from tests.tools import mock_request


class TestProduct(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_product()
        assert type(obj) == Product

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_products()
        assert all(type(x) == Product for x in obj)

        obj = api.get_products(56)
        assert type(obj) == Product and obj.id == 56

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_product(56)
        assert type(obj) == Product and obj.id == 56

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_product(56)
        assert type(obj) == Product and obj.id == 56

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Product.create_product(api)
        assert type(obj) == Product

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Product.get_products(api)
        assert all(type(x) == Product for x in obj)

        obj = Product.get_products(api, 56)
        assert type(obj) == Product and obj.id == 56

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Product.edit_product(api, 56)
        assert type(obj) == Product and obj.id == 56

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Product.delete_product(api, 56)
        assert type(obj) == Product and obj.id == 56

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Product.get_products(api, 56)
        assert type(obj) == Product and obj.id == 56

        obj = obj.update()
        assert type(obj) == Product and obj.id == 56

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_products(56)
        assert type(obj) == Product and obj.id == 56

        obj = obj.delete()
        assert type(obj) == Product and obj.id == 56