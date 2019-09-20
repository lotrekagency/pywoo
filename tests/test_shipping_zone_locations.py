import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.shipping_zone_locations import ShippingZoneLocation
from tests.tools import mock_request


class TestShippingLocation(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_shipping_zone_locations(1)
        assert all(type(x) == ShippingZoneLocation for x in obj)

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_shipping_zone_locations(1)
        assert all(type(x) == ShippingZoneLocation for x in obj)

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZoneLocation.get_shipping_zone_locations(api, 1)
        assert all(type(x) == ShippingZoneLocation for x in obj)

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZoneLocation.edit_shipping_zone_locations(api, 1)
        assert all(type(x) == ShippingZoneLocation for x in obj)