from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser


@ClassParser(url_class="shipping_methods")
class ShippingMethod(ApiObject):
    """
    Class for handling shipping methods objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-methods>`__
    """
    _ro_attributes = {'id', 'title', 'description'}

    @classmethod
    def get_shipping_methods(cls, api, id=''):
        """
        Get all or single shipping method by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a shipping method by id
        :type id: int, str
        :rtype: list of pywoo.models.shipping_methods.ShippingMethod,
            pywoo.models.shipping_methods.ShippingMethod
        """
        return api.get_shipping_methods(id)

    def refresh(self):
        """
        Refresh shipping method properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_shipping_methods(id=self.id).__dict__
