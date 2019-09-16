from utils.models import ApiObject


class ShippingZone(ApiObject):
    def __init__(self, id, name, order, api):
        super().__init__(api)
        self._id = id
        self.name = name
        self.order = order

    @property
    def id(self):
        return self._id