from mock import patch

from pywoo.pywoo import Api
from pywoo.models.tax_rates import TaxRate
from tests.tools import mock_request


@patch('requests.request', side_effect=mock_request)
def test_tax_rates():
    api = Api('fake_site_url', 'fake_consumer_key', 'fake_consumer_secret')

    tr = api.create_tax_rate(country="IT", state="Lazio", city="Roma", name="tassa")
    assert type(tr) == TaxRate
