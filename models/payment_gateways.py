from utils.models import ApiObject, ApiProperty
from utils.parse import to_json

class PaymentGateway(ApiObject):
    def __init__(self, id, title, description, order, enabled, method_title, method_description, method_supports,
                 settings, api):
        super().__init__(api)
        self._id = id
        self.title = title
        self.description = description
        self.order = order
        self.enabled = enabled
        self._method_title = method_title
        self._method_description = method_description
        self._method_supports = method_supports
        self.settings = settings

    @classmethod
    def get_payment_gateways(cls, api, id='', **params):
        return api.get_payment_gateways(id, **params)

    @classmethod
    def edit_payment_gateway(cls, api, id, **kwargs):
        return api.edit_payment_gateway(id, **kwargs)

    @classmethod
    def delete_payment_gateway(cls, api, id):
        return api.delete_payment_gateway(id)

    def update(self):
        return self._api.update_payment_gateway(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_payment_gateway(self.id)

    @property
    def id(self):
        return self._id

    @property
    def method_title(self):
        return self._method_title

    @property
    def method_description(self):
        return self._method_description

    @property
    def method_supports(self):
        return self._method_supports


class Setting(ApiProperty):
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

    @property
    def id(self):
        return self._id

    @property
    def label(self):
        return self._label

    @property
    def description(self):
        return self._description

    @property
    def type(self):
        return self._type

    @property
    def default(self):
        return self._default

    @property
    def tip(self):
        return self._tip

    @property
    def placeholder(self):
        return self._placeholder
