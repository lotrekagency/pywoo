import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.shipping_methods import ShippingMethod
from tests.tools import mock_request


class TestShippingMethod(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_shipping_methods()
        assert all(type(x) == ShippingMethod for x in obj)

        obj = api.get_shipping_methods(id='flat_rate')
        assert type(obj) == ShippingMethod and obj.id == 'flat_rate'

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingMethod.get_shipping_methods(api)
        assert all(type(x) == ShippingMethod for x in obj)

        obj = ShippingMethod.get_shipping_methods(api, id='flat_rate')
        assert type(obj) == ShippingMethod and obj.id == 'flat_rate'
    
    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_shipping_methods(id='flat_rate')
        assert type(obj) == ShippingMethod and obj.id == 'flat_rate'

        obj.refresh()
        assert type(obj) == ShippingMethod and obj.id == 'flat_rate'
