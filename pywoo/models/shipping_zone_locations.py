from pywoo.utils.models import ApiProperty
from pywoo.utils.parse import ClassParser


@ClassParser(url_class="locations")
class ShippingZoneLocation(ApiProperty):
    """
    Class for handling shipping zone locations objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-methods>`__
    """
    _rw_attributes = {'code', 'type'}

    @classmethod
    def get_shipping_zone_locations(cls, api, shipping_zone_id):
        """
        Get all or single shipping method by id

        :param api: API object
        :type api: pywoo.Api
        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :rtype: list of pywoo.models.shipping_zone_locations.ShippingZoneLocation,
            pywoo.models.shipping_zone_locations.ShippingZoneLocation
        """
        return api.get_shipping_zone_locations(shipping_zone_id)

    @classmethod
    def edit_shipping_zone_locations(cls, api, shipping_zone_id, shipping_locations=[]):
        """
        Change shipping locations by shippin zone id

        :param api: API object
        :type api: pywoo.Api
        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param shipping_locations: Shipping locations
        :type shipping_locations: list of dicts
        :rtype: list of pywoo.models.shipping_zone_locations.ShippingZoneLocation,
            pywoo.models.shipping_zone_locations.ShippingZoneLocation
        """
        return api.update_shipping_zone_locations(shipping_zone_id, shipping_locations)
