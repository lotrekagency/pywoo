from utils.models import ApiObject


class ShippingZoneMethods(ApiObject):
    def __init__(self, instance_id, title, order, enabled, method_id, method_title, method_description, settings, api):
        super().__init__(api)
        self._instance_id = instance_id
        self._title = title
        self.order = order
        self.enabled = enabled
        self._method_id = method_id
        self._method_title = method_title
        self._method_description = method_description
        self.settings = settings


class ShippingMethodSetting:
    def __init__(self, id=None, label=None, description=None, type=None, value=None, default=None, tip=None,
                 placeholder=None):
        self._id = id
        self._label = label
        self._description = description
        self._type = type
        self.value = value
        self._default = default
        self._tip = tip
        self._placeholder = placeholder
