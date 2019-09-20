import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.product_variations import ProductVariation
from tests.tools import mock_request


class TestProductVariation(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_product_variation(56)
        assert type(obj) == ProductVariation

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_variations(56)
        assert all(type(x) == ProductVariation for x in obj)

        obj = api.get_product_variations(56, 57)
        assert type(obj) == ProductVariation and obj.id == 57

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_product_variation(56, 57)
        assert type(obj) == ProductVariation and obj.id == 57

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_product_variation(56, 57)
        assert type(obj) == ProductVariation and obj.id == 57

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductVariation.create_product_variation(api, 56)
        assert type(obj) == ProductVariation

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductVariation.get_product_variations(api, 56)
        assert all(type(x) == ProductVariation for x in obj)

        obj = ProductVariation.get_product_variations(api, 56, 57)
        assert type(obj) == ProductVariation and obj.id == 57

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductVariation.edit_product_variation(api, 56, 57)
        assert type(obj) == ProductVariation and obj.id == 57

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductVariation.delete_product_variation(api, 56, 57)
        assert type(obj) == ProductVariation and obj.id == 57

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductVariation.get_product_variations(api, 56, 57)
        assert type(obj) == ProductVariation and obj.id == 57

        obj = obj.update()
        assert type(obj) == ProductVariation and obj.id == 57

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_variations(56, 57)
        assert type(obj) == ProductVariation and obj.id == 57

        obj = obj.delete()
        assert type(obj) == ProductVariation and obj.id == 57
