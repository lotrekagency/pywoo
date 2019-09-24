import unittest

from unittest.mock import Mock, patch

from pywoo import Api
from pywoo.models.coupon import Coupon
from .tools import mock_request


class TestCoupon(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_coupon()
        assert type(obj) == Coupon

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_coupons()
        assert all(type(x) == Coupon for x in obj)

        obj = api.get_coupons(id='112')
        assert type(obj) == Coupon and obj.id == 112

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_coupon(id='112')
        assert type(obj) == Coupon and obj.id == 112

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_coupon(id='112')
        assert type(obj) == Coupon and obj.id == 112

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Coupon.create_coupon(api)
        assert type(obj) == Coupon

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Coupon.get_coupons(api)
        assert all(type(x) == Coupon for x in obj)

        obj = Coupon.get_coupons(api, id='112')
        assert type(obj) == Coupon and obj.id == 112

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Coupon.edit_coupon(api, id='112')
        assert type(obj) == Coupon and obj.id == 112

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Coupon.delete_coupon(api, id='112')
        assert type(obj) == Coupon and obj.id == 112

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = Coupon.get_coupons(api, id='112')
        assert type(obj) == Coupon and obj.id == 112

        obj = obj.update()
        assert type(obj) == Coupon and obj.id == 112

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_coupons(id='112')
        assert type(obj) == Coupon and obj.id == 112

        obj = obj.delete()
        assert type(obj) == Coupon and obj.id == 112
