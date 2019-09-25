import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.orders import Order 
from .tools import mock_request

class TestOrder(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_order()
        assert type(obj) == Order

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_orders()
        assert all(type(x) == Order for x in obj)

        obj = api.get_orders(id='97')
        assert type(obj) == Order and obj.id == 97

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_order(id='97')
        assert type(obj) == Order and obj.id == 97

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_order(id='97')
        assert type(obj) == Order and obj.id == 97
    
    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Order.create_order(api)
        assert type(obj) == Order

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Order.get_orders(api)
        assert all(type(x) == Order for x in obj)

        obj = Order.get_orders(api, id='97')
        assert type(obj) == Order and obj.id == 97

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Order.edit_order(api, id='97')
        assert type(obj) == Order and obj.id == 97

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Order.delete_order(api, id='97')
        assert type(obj) == Order and obj.id == 97

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Order.get_orders(api, id='97')
        assert type(obj) == Order and obj.id == 97

        obj = obj.update()
        assert type(obj) == Order and obj.id == 97

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_orders(id='97')
        assert type(obj) == Order and obj.id == 97

        obj = obj.delete()
        assert type(obj) == Order and obj.id == 97
    
    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_orders(id='97')
        assert type(obj) == Order and obj.id == 97

        obj.refresh()
        assert type(obj) == Order and obj.id == 97



