import os

from pywoo.pywoo import Api
from pywoo.models.tax_rates import TaxRate


def test_tax_rates():
    api = Api(os.environ['SITE_URL'], os.environ['WOO_CONSUMER_KEY'], os.environ['WOO_CONSUMER_SECRET'])

    tr = api.create_tax_rate(country="IT", state="Lazio", city="Roma", name="tassa")
    assert tr.country == "IT"
    assert tr.name == "tassa"

    tr = api.get_tax_rates(tr.id)
    assert tr.country == "IT"
    assert tr.city == "ROMA"

    tr = TaxRate.edit_tax_rate(api, tr.id, country="DE")

    assert tr.country == "DE"

    tr_2 = TaxRate.get_tax_rates(api, tr.id)

    assert tr_2.country == "DE"

    tr = api.update_tax_rate(tr.id, priority=10)
    assert tr.priority == 10

    tr = api.delete_tax_rate(tr.id)

    tr = TaxRate.create_tax_rate(api, country="IT", state="Toscana", city="Firenze", name="fi")

    assert tr.state == "TOSCANA"

    tr.name = "eae"
    tr.shipping = True

    tr_2 = tr.update()

    assert tr_2.name == "eae"
    assert tr_2.shipping == True
