from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser


@ClassParser(url_class="shipping_methods")
class ShippingMethod(ApiObject):
    ro_attributes = {'id', 'title', 'description'}

    @classmethod
    def get_shipping_methods(cls, api, id='', **params):
        return api.get_shipping_methods(id, **params)
