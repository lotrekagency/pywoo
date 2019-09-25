import unittest

from mock import patch

from pywoo.pywoo import Api
from pywoo.models.product_tags import ProductTag
from tests.tools import mock_request


class TestProductTag(unittest.TestCase):

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.create_product_tag()
        assert type(obj) == ProductTag

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_tags()
        assert all(type(x) == ProductTag for x in obj)

        obj = api.get_product_tags(23)
        assert type(obj) == ProductTag and obj.id == 23

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.update_product_tag(23)
        assert type(obj) == ProductTag and obj.id == 23

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_api_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.delete_product_tag(23)
        assert type(obj) == ProductTag and obj.id == 23

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_post(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductTag.create_product_tag(api)
        assert type(obj) == ProductTag

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_get(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductTag.get_product_tags(api)
        assert all(type(x) == ProductTag for x in obj)

        obj = ProductTag.get_product_tags(api, 23)
        assert type(obj) == ProductTag and obj.id == 23

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_put(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductTag.edit_product_tag(api, 23)
        assert type(obj) == ProductTag and obj.id == 23

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_classmethod_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductTag.delete_product_tag(api, 23)
        assert type(obj) == ProductTag and obj.id == 23

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_update(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = ProductTag.get_product_tags(api, 23)
        assert type(obj) == ProductTag and obj.id == 23

        obj = obj.update()
        assert type(obj) == ProductTag and obj.id == 23

    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_delete(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_tags(23)
        assert type(obj) == ProductTag and obj.id == 23

        obj = obj.delete()
        assert type(obj) == ProductTag and obj.id == 23
    
    @patch('pywoo.pywoo.requests.api.request', side_effect=mock_request)
    def test_object_refresh(self, func):
        api = Api('', 'fake_consumer_key', 'fake_consumer_secret')

        obj = api.get_product_tags(23)
        assert type(obj) == ProductTag and obj.id == 23

        obj.refresh()
        assert type(obj) == ProductTag and obj.id == 23
