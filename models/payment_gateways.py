from utils.models import ApiObject, ApiProperty


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
