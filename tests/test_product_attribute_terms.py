import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.products_attribute_terms import ProductAttributeTerm
from .tools import mock_request


class TestProductAttributeTerm(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_product_attribute_term(1)
        assert type(obj) == ProductAttributeTerm

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_attribute_terms(1)
        assert all(type(x) == ProductAttributeTerm for x in obj)

        obj = api.get_product_attribute_terms(1, 26)
        assert type(obj) == ProductAttributeTerm and obj.id == 26

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_product_attribute_term(1, 26)
        assert type(obj) == ProductAttributeTerm and obj.id == 26

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductAttributeTerm.create_product_attribute_term(api, 1)
        assert type(obj) == ProductAttributeTerm

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductAttributeTerm.get_product_attribute_terms(api, 1)
        assert all(type(x) == ProductAttributeTerm for x in obj)

        obj = ProductAttributeTerm.get_product_attribute_terms(api, 1, 26)
        assert type(obj) == ProductAttributeTerm and obj.id == 26

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductAttributeTerm.delete_product_attribute_term(api, 1, 26)
        assert type(obj) == ProductAttributeTerm and obj.id == 26

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_attribute_terms(1, 26)
        assert type(obj) == ProductAttributeTerm and obj.id == 26

        obj = obj.delete()
        assert type(obj) == ProductAttributeTerm and obj.id == 26



