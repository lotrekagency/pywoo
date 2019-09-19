import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.payment_gateways import PaymentGateway 
from .tools import mock_request

class TestPaymentGateways(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_payment_gateways()
        assert all(type(x) == PaymentGateway for x in obj)

        obj = api.get_payment_gateways(id='bacs')
        assert type(obj) == PaymentGateway and obj.id == 'bacs'

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_payment_gateway(id='bacs')
        assert type(obj) == PaymentGateway and obj.id == 'bacs'

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = PaymentGateway.get_payment_gateways(api)
        assert all(type(x) == PaymentGateway for x in obj)

        obj = PaymentGateway.get_payment_gateways(api, id='bacs')
        assert type(obj) == PaymentGateway and obj.id == 'bacs'

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = PaymentGateway.edit_payment_gateway(api, id='bacs')
        assert type(obj) == PaymentGateway and obj.id == 'bacs'

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = PaymentGateway.get_payment_gateways(api, id='bacs')
        assert type(obj) == PaymentGateway and obj.id == 'bacs'

        obj = obj.update()
        assert type(obj) == PaymentGateway and obj.id == 'bacs'



