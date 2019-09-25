import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.product_categories import ProductCategory 
from .tools import mock_request

class TestProductCategories(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_product_category()
        assert type(obj) == ProductCategory

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_categories()
        assert all(type(x) == ProductCategory for x in obj)

        obj = api.get_product_categories(id='18')
        assert type(obj) == ProductCategory and obj.id == 18

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_product_category(id='18')
        assert type(obj) == ProductCategory and obj.id == 18

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_product_category(id='18')
        assert type(obj) == ProductCategory and obj.id == 18
    
    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductCategory.create_product_category(api)
        assert type(obj) == ProductCategory

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductCategory.get_product_categories(api)
        assert all(type(x) == ProductCategory for x in obj)

        obj = ProductCategory.get_product_categories(api, id='18')
        assert type(obj) == ProductCategory and obj.id == 18

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductCategory.edit_product_category(api, id='18')
        assert type(obj) == ProductCategory and obj.id == 18

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductCategory.delete_product_category(api, id='18')
        assert type(obj) == ProductCategory and obj.id == 18

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductCategory.get_product_categories(api, id='18')
        assert type(obj) == ProductCategory and obj.id == 18

        obj = obj.update()
        assert type(obj) == ProductCategory and obj.id == 18

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_categories(id='18')
        assert type(obj) == ProductCategory and obj.id == 18

        obj = obj.delete()
        assert type(obj) == ProductCategory and obj.id == 18

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_categories(id='18')
        assert type(obj) == ProductCategory and obj.id == 18

        obj.refresh()
        assert type(obj) == ProductCategory and obj.id == 18

