from pywoo.utils.models import ApiProperty
from pywoo.utils.parse import ClassParser


@ClassParser(url_class="locations")
class ShippingZoneLocation(ApiProperty):
    rw_attributes = {'code', 'type'}
    
    @classmethod
    def get_shipping_zone_locations(cls, api, shipping_zone_id):
        return api.get_shipping_zone_locations(shipping_zone_id)

    @classmethod
    def edit_shipping_zone_locations(cls, api, shipping_zone_id, shipping_locations=[]):
        return api.update_shipping_zone_locations(shipping_zone_id, shipping_locations)
    
    def refresh(self):
        self.__dict__ = self._api.get_shipping_zone_locations(id=self.id).__dict__
