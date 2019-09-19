from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser


@ClassParser()
class ShippingMethod(ApiObject):
    def __init__(self, id, title, description, api, url):
        super().__init__(api, url)
        self._id = id
        self._title = title
        self._description = description

    @classmethod
    def get_shipping_methods(cls, api, id='', **params):
        return api.get_orders(id, **params)

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description
