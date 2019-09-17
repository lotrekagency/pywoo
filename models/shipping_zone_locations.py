from utils.models import ApiProperty


class ShippingZoneLocation(ApiProperty):
    def __init__(self, code, type):
        self.code = code
        self.type = type