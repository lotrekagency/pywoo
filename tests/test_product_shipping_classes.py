import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.product_shipping_classes import ProductShipping
from tests.tools import mock_request


class TestProductShipping(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_product_shipping_class()
        assert type(obj) == ProductShipping

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_shipping_classes()
        assert all(type(x) == ProductShipping for x in obj)

        obj = api.get_product_shipping_classes(24)
        assert type(obj) == ProductShipping and obj.id == 24

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_product_shipping_class(24)
        assert type(obj) == ProductShipping and obj.id == 24

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_product_shipping_class(24)
        assert type(obj) == ProductShipping and obj.id == 24

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductShipping.create_product_shipping_class(api)
        assert type(obj) == ProductShipping

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductShipping.get_product_shipping_classes(api)
        assert all(type(x) == ProductShipping for x in obj)

        obj = ProductShipping.get_product_shipping_classes(api, 24)
        assert type(obj) == ProductShipping and obj.id == 24

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductShipping.edit_product_shipping_class(api, 24)
        assert type(obj) == ProductShipping and obj.id == 24

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductShipping.delete_product_shipping_class(api, 24)
        assert type(obj) == ProductShipping and obj.id == 24

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductShipping.get_product_shipping_classes(api, 24)
        assert type(obj) == ProductShipping and obj.id == 24

        obj = obj.update()
        assert type(obj) == ProductShipping and obj.id == 24

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_shipping_classes(24)
        assert type(obj) == ProductShipping and obj.id == 24

        obj = obj.delete()
        assert type(obj) == ProductShipping and obj.id == 24
