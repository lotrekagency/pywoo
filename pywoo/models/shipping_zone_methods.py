from re import search

from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="methods")
class ShippingZoneMethod(ApiObject):
    """
    Class for handling shipping zone methods objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-method-properties>`__
    """
    _ro_attributes = {'instance_id', 'title', 'method_id', 'method_title', 'method_description'}
    _rw_attributes = {'order', 'enabled', 'settings'}

    @classmethod
    def get_shipping_zone_methods(cls, api, shipping_zone_id, id=''):
        """
        Get all or single shipping zone method by id

        :param api: API object
        :type api: pywoo.Api
        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param id: If specified gets a shipping zone method by id
        :type id: int, str
        :rtype: list of pywoo.models.shipping_zone_methods.ShippingZoneMethod,
            pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return api.get_shipping_zone_methods(shipping_zone_id, id)

    @classmethod
    def create_shipping_zone_method(cls, api, shipping_zone_id, **data):
        """
        Create shipping zone method
        
        :param api: API object
        :type api: pywoo.Api
        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param data: Shipping zone method properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-method-properties>`__)
        :rtype: pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return api.create_shipping_zone_method(shipping_zone_id, **data)

    @classmethod
    def edit_shipping_zone_method(cls, api, shipping_zone_id, id, **data):
        """
        Change shipping zone method's properties

        :param api: API object
        :type api: pywoo.Api
        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param id: Shipping zone method id
        :type id: int, str
        :param data: Shipping zone method properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-method-properties>`__)
        :rtype: pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return api.update_shipping_zone_method(shipping_zone_id, id, **data)

    @classmethod
    def delete_shipping_zone_method(cls, api, shipping_zone_id, id):
        """
        Delete shipping zone method by id

        :param api: API object
        :type api: pywoo.Api
        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param id: Shipping zone method id
        :type id: int, str
        :rtype: pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return api.delete_shipping_zone_method(shipping_zone_id, id)

    def update(self):
        """
        Push shipping zone method properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.shipping_zone_methods.ShippingZoneMethod.refresh()` method or use the returned object
        which is updated.

        :return: Shipping zone method with updated properties coming from the REST API
        :rtype: pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return self._api.update_shipping_zone_method(self.shipping_zone_id, **to_dict(self))

    def delete(self):
        """
        Deletes shipping zone method. The object can't be used anymore after its deletion.

        :return: Deleted shipping zone method
        :rtype: pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return self._api.delete_shipping_zone_method(self.shipping_zone_id, self.instance_id)

    def refresh(self):
        """
        Refresh shipping zone method properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_shipping_zone_methods(shipping_zone_id=self.shipping_zone_id, id=self.id).__dict__

    @property
    def shipping_zone_id(self):
        return search(r"shipping\/zones\/(\d+)\/.*", self._url).group(1)


@ClassParser(url_class="methods")
class ShippingMethodSetting(ApiProperty):
    """
    Class for handling shipping method settings inside :class:`~pywoo.models.shipping_zone_methods.ShippingZoneMethod` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-method-settings-properties>`__
    """
    _ro_attributes = {'id', 'label', 'description', 'type', 'default', 'tip', 'placeholder'}
    _rw_attributes = {'value'}
