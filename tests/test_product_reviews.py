import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.product_reviews import ProductReview
from tests.tools import mock_request


class TestProductReview(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_product_review()
        assert type(obj) == ProductReview

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_reviews()
        assert all(type(x) == ProductReview for x in obj)

        obj = api.get_product_reviews(42)
        assert type(obj) == ProductReview and obj.id == 42

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_product_review(42)
        assert type(obj) == ProductReview and obj.id == 42

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_product_review(42)
        assert type(obj) == ProductReview and obj.id == 42

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductReview.create_product_review(api)
        assert type(obj) == ProductReview

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductReview.get_product_reviews(api)
        assert all(type(x) == ProductReview for x in obj)

        obj = ProductReview.get_product_reviews(api, 42)
        assert type(obj) == ProductReview and obj.id == 42

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductReview.edit_product_review(api, 42)
        assert type(obj) == ProductReview and obj.id == 42

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductReview.delete_product_review(api, 42)
        assert type(obj) == ProductReview and obj.id == 42

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductReview.get_product_reviews(api, 42)
        assert type(obj) == ProductReview and obj.id == 42

        obj = obj.update()
        assert type(obj) == ProductReview and obj.id == 42

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_reviews(42)
        print(obj)
        assert type(obj) == ProductReview and obj.id == 42

        obj = obj.delete()
        assert type(obj) == ProductReview and obj.id == 42
