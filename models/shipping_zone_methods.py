from re import search

from utils.models import ApiObject
from utils.parse import to_json, ClassParser


@ClassParser()
class ShippingZoneMethods(ApiObject):
    def __init__(self, instance_id, title, order, enabled, method_id, method_title, method_description, settings, api,
                 url):
        super().__init__(api, url)
        self._instance_id = instance_id
        self._title = title
        self.order = order
        self.enabled = enabled
        self._method_id = method_id
        self._method_title = method_title
        self._method_description = method_description
        self.settings = settings

    @classmethod
    def get_shipping_zone_method(cls, api, shipping_zone_id, id=''):
        return api.get_shipping_zone_methods(shipping_zone_id, id)

    @classmethod
    def create_shipping_zone_method(cls, api, shipping_zone_id, **kwargs):
        return api.create_shipping_zone_method(shipping_zone_id, **kwargs)

    @classmethod
    def edit_shipping_zone_method(cls, api, shipping_zone_id, id, **kwargs):
        return api.update_shipping_zone_method(shipping_zone_id, id, **kwargs)

    @classmethod
    def delete_shipping_zone_method(cls, api, shipping_zone_id, id):
        return api.delete_shipping_zone_method(shipping_zone_id, id)

    def update(self):
        return self._api.update_shipping_zone_method(self.shipping_zone_id, self.instance_id, **to_json(self))

    def delete(self):
        return self._api.delete_shipping_zone_method(self.shipping_zone_id, self.instance_id)

    @property
    def instance_id(self):
        return self._instance_id

    @property
    def title(self):
        return self._title

    @property
    def method_title(self):
        return self._method_title

    @property
    def method_description(self):
        return self._method_description

    @property
    def shipping_zone_id(self):
        return search(r"shipping\/zones\/(\d+)\/.*", self._url).group(1)
