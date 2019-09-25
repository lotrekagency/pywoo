import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.orders_notes import OrderNote 
from .tools import mock_request

class TestOrderNote(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_order_note(order_id=97)
        assert type(obj) == OrderNote

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_order_notes(order_id='97')
        assert all(type(x) == OrderNote for x in obj)

        obj = api.get_order_notes(order_id='97', id='108')
        assert type(obj) == OrderNote and obj.id == 108

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_order_note(order_id='97', id='108')
        assert type(obj) == OrderNote and obj.id == 108
    
    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = OrderNote.create_order_note(api, order_id='97')
        assert type(obj) == OrderNote

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = OrderNote.get_order_notes(api, order_id='97')
        assert all(type(x) == OrderNote for x in obj)

        obj = OrderNote.get_order_notes(api, order_id='97', id='108')
        assert type(obj) == OrderNote and obj.id == 108

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = OrderNote.delete_order_note(api, order_id='97', id='108')
        assert type(obj) == OrderNote and obj.id == 108

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_order_notes(order_id='97', id='108')
        assert type(obj) == OrderNote and obj.id == 108

        obj = obj.delete()
        assert type(obj) == OrderNote and obj.id == 108

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_order_notes(order_id='97', id='108')
        assert type(obj) == OrderNote and obj.id == 108

        obj.refresh()
        assert type(obj) == OrderNote and obj.id == 108



