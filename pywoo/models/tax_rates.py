from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_json, ClassParser


@ClassParser()
class TaxRate(ApiObject):
    def __init__(self, id, country, state, postcode, city, rate, name, priority, compound, shipping, order, class_,
                 api, url):
        super().__init__(api, url)
        self._id = id
        self.country = country
        self.state = state
        self.postcode = postcode
        self.city = city
        self.rate = rate
        self.name = name
        self.priority = priority
        self.compound = compound
        self.shipping = shipping
        self.order = order
        self.class_ = class_

    @classmethod
    def get_tax_rates(cls, api, id='', **params):
        return api.get_tax_rates(id, **params)

    @classmethod
    def create_tax_rate(cls, api, **kwargs):
        return api.create_tax_rate(**kwargs)

    @classmethod
    def edit_tax_rate(cls, api, id, **kwargs):
        return api.update_tax_rate(id, **kwargs)

    @classmethod
    def delete_tax_rate(cls, api, id):
        return api.delete_tax_rate(id)

    def update(self):
        return self._api.update_tax_rate(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_tax_rate(self.id)

    @property
    def id(self):
        return self._id
