from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_json, ClassParser


@ClassParser(url_class="zones")
class ShippingZone(ApiObject):
    ro_attributes = {'id'}
    rw_attributes = {'name', 'order'}

    @classmethod
    def get_shipping_zone(cls, api, id=''):
        return api.get_shipping_zones(id)

    @classmethod
    def create_shipping_zone(cls, api, **kwargs):
        return api.create_shipping_zone(**kwargs)

    @classmethod
    def edit_shipping_zone(cls, api, id, **kwargs):
        return api.update_shipping_zone(id, **kwargs)

    @classmethod
    def delete_shipping_zone(cls, api, id):
        return api.delete_shipping_zone(id)

    def update(self):
        return self._api.update_shipping_zone(**to_json(self))

    def delete(self):
        return self._api.delete_shipping_zone(self.id)
    
    def refresh(self):
        self.__dict__ = self._api.get_shipping_zones(id=self.id).__dict__
