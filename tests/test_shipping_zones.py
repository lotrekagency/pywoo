import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.shipping_zones import ShippingZone
from tests.tools import mock_request


class TestShippingZone(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_shipping_zone()
        assert type(obj) == ShippingZone

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_shipping_zones()
        assert all(type(x) == ShippingZone for x in obj)

        obj = api.get_shipping_zones(id='1')
        assert type(obj) == ShippingZone and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_shipping_zone(id='1')
        assert type(obj) == ShippingZone and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_shipping_zone(id='1')
        assert type(obj) == ShippingZone and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZone.create_shipping_zone(api)
        assert type(obj) == ShippingZone

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZone.get_shipping_zone(api)
        assert all(type(x) == ShippingZone for x in obj)

        obj = ShippingZone.get_shipping_zone(api, id='1')
        assert type(obj) == ShippingZone and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZone.edit_shipping_zone(api, id='1')
        assert type(obj) == ShippingZone and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZone.delete_shipping_zone(api, id='1')
        assert type(obj) == ShippingZone and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ShippingZone.get_shipping_zone(api, id='1')
        assert type(obj) == ShippingZone and obj.id == 1

        obj = obj.update()
        assert type(obj) == ShippingZone and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_shipping_zones(id='1')
        assert type(obj) == ShippingZone and obj.id == 1

        obj = obj.delete()
        assert type(obj) == ShippingZone and obj.id == 1

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_shipping_zones(id='1')
        assert type(obj) == ShippingZone and obj.id == 1

        obj.refresh()
        assert type(obj) == ShippingZone and obj.id == 1
