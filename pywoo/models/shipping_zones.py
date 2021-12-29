from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="zones")
class ShippingZone(ApiObject):
    """
    Class for handling shipping zone objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-zones>`__
    """
    _ro_attributes = {'id'}
    _rw_attributes = {'name', 'order'}

    @classmethod
    def get_shipping_zone(cls, api, id=''):
        """
        Get all or single shipping zone by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a shipping zone by id
        :type id: int, str
        :rtype: list of pywoo.models.shipping_zone.ShippingZone,
            pywoo.models.shipping_zone.ShippingZone
        """
        return api.get_shipping_zones(id)

    @classmethod
    def create_shipping_zone(cls, api, **data):
        """
        Create shipping zone
        
        :param api: API object
        :type api: pywoo.Api
        :param data: Shipping zone properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-zone-properties>`__)
        :rtype: pywoo.models.shipping_zone.ShippingZone
        """
        return api.create_shipping_zone(**data)

    @classmethod
    def edit_shipping_zone(cls, api, id, **data):
        """
        Change shipping zone's properties

        :param api: API object
        :type api: pywoo.Api
        :param id: Shipping zone id
        :type id: int, str
        :param data: Shipping zone properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-zone-properties>`__)
        :rtype: pywoo.models.shipping_zone.ShippingZone
        """
        return api.update_shipping_zone(id, **data)

    @classmethod
    def delete_shipping_zone(cls, api, id):
        """
        Delete shipping zone by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Shipping zone id
        :type id: int, str
        :rtype: pywoo.models.shipping_zone.ShippingZone
        """
        return api.delete_shipping_zone(id)

    def update(self):
        """
        Push shipping zone properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.shipping_zone.ShippingZone.refresh()` method or use the returned object
        which is updated.

        :return: Shipping zone with updated properties coming from the REST API
        :rtype: pywoo.models.shipping_zone.ShippingZone
        """
        return self._api.update_shipping_zone(**to_dict(self))

    def delete(self):
        """
        Deletes shipping zone. The object can't be used anymore after its deletion.

        :return: Deleted shipping zone
        :rtype: pywoo.models.shipping_zone.ShippingZone
        """
        return self._api.delete_shipping_zone(self.id)

    def refresh(self):
        """
        Refresh shipping zone properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_shipping_zones(id=self.id).__dict__
