from utils.models import ApiProperty


class ShippingZoneLocation(ApiProperty):
    def __init__(self, code, type):
        self.code = code
        self.type = type
    
    @classmethod
    def get_shipping_zone_locations(cls, api, shipping_zone_id=''):
        return api.get_shipping_zone_locations(shipping_zone_id)
    