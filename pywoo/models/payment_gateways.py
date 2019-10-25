from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import ClassParser

from pywoo.utils.parse import to_dict


@ClassParser(url_classes=["payment_gateways"])
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
        self.__dict__ = self._api.update_payment_gateway(**to_dict(self)).__dict__
    
    def refresh(self):
        self.__dict__ = self._api.get_payment_gateways(id=self.id).__dict__


@ClassParser(url_classes=["payment_gateways"])
class PaymentGatewaySetting(ApiProperty):
    ro_attributes = {'id', 'label', 'description', 'type', 'default', 'tip', 'placeholder'}
    rw_attributes = {'value'}
