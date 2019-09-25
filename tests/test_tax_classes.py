import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.tax_classes import TaxClass
from tests.tools import mock_request


class TestTaxClass(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_tax_class()
        assert type(obj) == TaxClass

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_tax_classes()
        assert all(type(x) == TaxClass for x in obj)

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_tax_class(id='tariffa')
        assert type(obj) == TaxClass and obj.slug == 'tariffa'

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = TaxClass.create_tax_class(api)
        assert type(obj) == TaxClass

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = TaxClass.get_tax_classes(api)
        assert all(type(x) == TaxClass for x in obj)

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = TaxClass.delete_tax_class(api, slug='tariffa')
        assert type(obj) == TaxClass and obj.slug == 'tariffa'

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_tax_classes()[-1]

        obj = obj.delete()
        assert type(obj) == TaxClass and obj.slug == 'tariffa'

