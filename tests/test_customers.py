import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.customers import Customer 
from .tools import mock_request

class TestCustomer(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_customer()
        assert type(obj) == Customer

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_customers()
        assert all(type(x) == Customer for x in obj)

        obj = api.get_customers(id='4')
        assert type(obj) == Customer and obj.id == 4

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_customer(id='4')
        assert type(obj) == Customer and obj.id == 4

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_customer(id='4')
        assert type(obj) == Customer and obj.id == 4
    
    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Customer.create_customer(api)
        assert type(obj) == Customer

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Customer.get_customers(api)
        assert all(type(x) == Customer for x in obj)

        obj = Customer.get_customers(api, id='4')
        assert type(obj) == Customer and obj.id == 4

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Customer.edit_customer(api, id='4')
        assert type(obj) == Customer and obj.id == 4

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Customer.delete_customer(api, id='4')
        assert type(obj) == Customer and obj.id == 4

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Customer.get_customers(api, id='4')
        assert type(obj) == Customer and obj.id == 4

        obj = obj.update()
        assert type(obj) == Customer and obj.id == 4

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_customers(id='4')
        assert type(obj) == Customer and obj.id == 4

        obj = obj.delete()
        assert type(obj) == Customer and obj.id == 4

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_customers(id='4')
        assert type(obj) == Customer and obj.id == 4

        obj.refresh()
        assert type(obj) == Customer and obj.id == 4



