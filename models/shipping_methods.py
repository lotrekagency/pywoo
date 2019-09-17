from utils.models import ApiObject
from utils.parse import to_json


class ShippingMethod(ApiObject):
    def __init__(self, id, title, description, api, url):
        super().__init__(api, url)
        self._id = id
        self._title = title
        self._description = description

    @classmethod
    def get_shipping_methods(cls, api, id=''):
        return api.get_shipping_method(id)

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

