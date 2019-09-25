from re import search

from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_json, ClassParser


@ClassParser(url_class="methods")
class ShippingZoneMethod(ApiObject):
    ro_attributes = {'instance_id', 'title', 'method_id', 'method_title', 'method_description'}
    rw_attributes = {'order', 'enabled', 'settings'}

    @classmethod
    def get_shipping_zone_methods(cls, api, shipping_zone_id, id=''):
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
        return self._api.update_shipping_zone_method(self.shipping_zone_id, **to_json(self))

    def delete(self):
        return self._api.delete_shipping_zone_method(self.shipping_zone_id, self.instance_id)

    def refresh(self):
        self.__dict__ = self._api.get_shipping_zone_methods(shipping_zone_id=self.shipping_zone_id, id=self.id).__dict__

    @property
    def shipping_zone_id(self):
        return search(r"shipping\/zones\/(\d+)\/.*", self._url).group(1)


@ClassParser(url_class="methods")
class PaymentGatewaySetting(ApiProperty):
    ro_attributes = {'id', 'label', 'description', 'type', 'default', 'tip', 'placeholder'}
    rw_attributes = {'value'}
