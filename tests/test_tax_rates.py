import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.tax_rates import TaxRate
from tests.tools import mock_request


class TestTaxRate(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_tax_rate()
        assert type(obj) == TaxRate

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_tax_rates()
        assert all(type(x) == TaxRate for x in obj)

        obj = api.get_tax_rates(id='2')
        assert type(obj) == TaxRate and obj.id == 2

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_tax_rate(id='2')
        assert type(obj) == TaxRate and obj.id == 2

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_tax_rate(id='2')
        assert type(obj) == TaxRate and obj.id == 2

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = TaxRate.create_tax_rate(api)
        assert type(obj) == TaxRate

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = TaxRate.get_tax_rates(api)
        assert all(type(x) == TaxRate for x in obj)

        obj = TaxRate.get_tax_rates(api, id='2')
        assert type(obj) == TaxRate and obj.id == 2

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = TaxRate.edit_tax_rate(api, id='2')
        assert type(obj) == TaxRate and obj.id == 2

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = TaxRate.delete_tax_rate(api, id='2')
        assert type(obj) == TaxRate and obj.id == 2

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = TaxRate.get_tax_rates(api, id='2')
        assert type(obj) == TaxRate and obj.id == 2

        obj = obj.update()
        assert type(obj) == TaxRate and obj.id == 2

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_tax_rates(id='2')
        assert type(obj) == TaxRate and obj.id == 2

        obj = obj.delete()
        assert type(obj) == TaxRate and obj.id == 2
