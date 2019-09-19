from mock import patch

from pywoo import Api
from pywoo.models.tax_classes import TaxClass
from tests.tools import mock_request


@patch('requests.request', side_effect=mock_request)
def test_tax_classes():
    api = Api('fake_site_url', 'fake_consumer_key', 'fake_consumer_secret')

    tc = api.create_tax_class()
    assert type(tc) == TaxClass
