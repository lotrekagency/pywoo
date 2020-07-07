from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import ClassParser

from pywoo.utils.parse import to_dict


@ClassParser(url_class="payment_gateways")
class PaymentGateway(ApiObject):
    """
    Class for handling payment gateway objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#payment-gateway-properties>`__
    """
    _ro_attributes = {'id', 'method_title', 'method_description'}
    _rw_attributes = {'title', 'description', 'order', 'enabled', 'settings'}

    @classmethod
    def get_payment_gateways(cls, api, id=''):
        """
        Get all or a single payment gateway by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a payment gateway by id
        :type id: int, str
        :rtype: list of pywoo.models.payment_gateways.PaymentGateway, pywoo.models.payment_gateways.PaymentGateway
        """
        return api.get_payment_gateways(id)

    @classmethod
    def edit_payment_gateway(cls, api, id, **data):
        """
        Change payment gateway's properties

        :param api: API object
        :type api: pywoo.Api
        :param id: Payment gateway id
        :type id: int, str
        :param data: Payment gateway properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#payment-gateway-properties>`__)
        :rtype: pywoo.models.payment_gateways.PaymentGateway
        """
        return api.update_payment_gateway(id, **data)

    def update(self):
        """
        Push payment gateway properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.payment_gateways.PaymentGateway.refresh()` method or use the returned object
        which is updated.

        :return: Payment gateway with updated properties coming from the REST API
        :rtype: pywoo.models.payment_gateways.PaymentGateway
        """
        return self._api.update_payment_gateway(**to_dict(self))

    def refresh(self):
        """
        Refresh payment gateway properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_payment_gateways(id=self.id).__dict__


@ClassParser(url_class="payment_gateways")
class PaymentGatewaySetting(ApiProperty):
    """
    Class for handling payment gateway settings inside :class:`~pywoo.models.payment_gateways.PaymentGateway` objects

    `List of parameters
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#payment-gateway-settings-properties>`__
    """
    _ro_attributes = {'id', 'label', 'description', 'type', 'default', 'tip', 'placeholder'}
    _rw_attributes = {'value'}
