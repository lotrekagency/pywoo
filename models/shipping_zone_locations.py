from utils.models import ApiObject


class ShippingZoneLocation(ApiObject):
    def __init__(self, code, type, api):
        super().__init__(api)
        self.code = code
        self.type = type