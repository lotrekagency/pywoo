import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.refunds import Refund 
from .tools import mock_request

class TestRefund(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_refund(order_id='97')
        assert type(obj) == Refund

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_refunds(order_id='97')
        assert all(type(x) == Refund for x in obj)

        obj = api.get_refunds(order_id='97', id='141')
        assert type(obj) == Refund and obj.id == 141

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_refund(order_id='97', id='141')
        assert type(obj) == Refund and obj.id == 141
    
    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Refund.create_refund(api, order_id='97')
        assert type(obj) == Refund

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Refund.get_refunds(api, order_id='97')
        assert all(type(x) == Refund for x in obj)

        obj = Refund.get_refunds(api, order_id='97', id='141')
        assert type(obj) == Refund and obj.id == 141

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Refund.delete_refund(api, order_id='97', id='141')
        assert type(obj) == Refund and obj.id == 141

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_refunds(order_id='97', id='141')
        assert type(obj) == Refund and obj.id == 141

        obj = obj.delete()
        assert type(obj) == Refund and obj.id == 141

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_refunds(order_id='97', id='141')
        assert type(obj) == Refund and obj.id == 141

        obj.refresh()
        assert type(obj) == Refund and obj.id == 141



