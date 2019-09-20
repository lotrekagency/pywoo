import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.shipping_zone_methods import ShippingZoneMethod
from tests.tools import mock_request


class TestShippingZoneMethod(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_shipping_zone_method(1)
        assert type(obj) == ShippingZoneMethod

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_shipping_zone_methods(1)
        assert all(type(x) == ShippingZoneMethod for x in obj)

        obj = api.get_shipping_zone_methods(1, 1)
        assert type(obj) == ShippingZoneMethod and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_shipping_zone_method(1, 1)
        assert type(obj) == ShippingZoneMethod and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_shipping_zone_method(1, 1)
        assert type(obj) == ShippingZoneMethod and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZoneMethod.create_shipping_zone_method(api, 1)
        assert type(obj) == ShippingZoneMethod

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZoneMethod.get_shipping_zone_methods(api, 1)
        assert all(type(x) == ShippingZoneMethod for x in obj)

        obj = ShippingZoneMethod.get_shipping_zone_methods(api, 1, 1)
        assert type(obj) == ShippingZoneMethod and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZoneMethod.edit_shipping_zone_method(api, 1, 1)
        assert type(obj) == ShippingZoneMethod and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZoneMethod.delete_shipping_zone_method(api, 1, 1)
        assert type(obj) == ShippingZoneMethod and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZoneMethod.get_shipping_zone_methods(api, 1, 1)
        print(obj)
        assert type(obj) == ShippingZoneMethod and obj.id == 1

        obj = obj.update()
        assert type(obj) == ShippingZoneMethod and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_shipping_zone_methods(1, 1)
        assert type(obj) == ShippingZoneMethod and obj.id == 1

        obj = obj.delete()
        assert type(obj) == ShippingZoneMethod and obj.id == 1
