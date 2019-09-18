from utils.models import ApiProperty
from utils.parse import ClassParser


@ClassParser()
class ShippingZoneLocation(ApiProperty):
    def __init__(self, code, type):
        self.code = code
        self.type = type