from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import ClassParser

from pywoo.utils.parse import to_json


@ClassParser(url="payment_gateways")
class PaymentGateway(ApiObject):
    ro_attributes = {'id', 'method_title', 'method_description', 'method_supports'}
    rw_attributes = {'title', 'description', 'order', 'enabled', 'settings'}

    @classmethod
    def get_payment_gateways(cls, api, id='', **params):
        return api.get_payment_gateways(id, **params)

    @classmethod
    def edit_payment_gateway(cls, api, id, **kwargs):
        return api.update_payment_gateway(id, **kwargs)

    def update(self):
        return self._api.update_payment_gateway(self.id, **to_json(self))


@ClassParser(url="payment_gateways")
class PaymentGatewaySetting(ApiProperty):
    ro_attributes = {'id', 'label', 'description', 'type', 'default', 'tip', 'placeholder'}
    rw_attributes = {'value'}
