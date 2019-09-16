from utils.models import ApiObject


class TaxRate(ApiObject):
    def __init__(self, id, country, state, postcode, city, rate, name, priority, compound, shipping, order, class_,
                 api):
        super().__init__(api)
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

    @property
    def id(self):
        return self._id
