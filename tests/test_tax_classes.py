import os

from pywoo import Api
from pywoo.models.tax_classes import TaxClass


def test_tax_classes():
    api = Api(os.environ['SITE_URL'], os.environ['WOO_CONSUMER_KEY'], os.environ['WOO_CONSUMER_SECRET'])

    tc = api.create_tax_class(name="qwertyuiopa")
    assert tc.name == "qwertyuiopa"

    tcs = api.get_tax_classes()
    assert any(x.name == "qwertyuiopa" for x in tcs) == True

    tc_2 = TaxClass.create_tax_class(api, name="poiuytre")
    assert tc_2.name == "poiuytre"

    tcs = TaxClass.get_tax_classes(api)
    assert any(x.name == "poiuytre" for x in tcs) == True

    tc_2.delete()

    TaxClass.delete_tax_rate(api, tc.slug)

    assert all(x.name != "qwertyuiopa" and x.name != "poiuytre" for x in api.get_tax_classes())
