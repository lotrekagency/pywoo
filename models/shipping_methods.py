from utils.models import ApiObject


class ShippingMethod(ApiObject):
    def __init__(self, id, title, description, api):
        super().__init__(api)
        self._id = id
        self._title = title
        self._description = description

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

