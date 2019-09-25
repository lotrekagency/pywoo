import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.product_attributes import ProductAttribute
from .tools import mock_request


class TestProductAttribute(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_product_attribute()
        assert type(obj) == ProductAttribute

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_attributes()
        assert all(type(x) == ProductAttribute for x in obj)

        obj = api.get_product_attributes(1)
        assert type(obj) == ProductAttribute and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_product_attribute(1)
        assert type(obj) == ProductAttribute and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_product_attribute(1)
        assert type(obj) == ProductAttribute and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductAttribute.create_product_attribute(api)
        assert type(obj) == ProductAttribute

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductAttribute.get_product_attributes(api)
        assert all(type(x) == ProductAttribute for x in obj)

        obj = ProductAttribute.get_product_attributes(api, 1)
        assert type(obj) == ProductAttribute and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductAttribute.edit_product_attribute(api, 1)
        assert type(obj) == ProductAttribute and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductAttribute.delete_product_attribute(api, 1)
        assert type(obj) == ProductAttribute and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductAttribute.get_product_attributes(api, 1)
        assert type(obj) == ProductAttribute and obj.id == 1

        obj = obj.update()
        assert type(obj) == ProductAttribute and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_attributes(1)
        assert type(obj) == ProductAttribute and obj.id == 1

        obj = obj.delete()
        assert type(obj) == ProductAttribute and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_attributes(1)
        assert type(obj) == ProductAttribute and obj.id == 1

        obj.refresh()
        assert type(obj) == ProductAttribute and obj.id == 1



