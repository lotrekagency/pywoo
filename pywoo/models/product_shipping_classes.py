from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser, to_json


@ClassParser(url_class="shipping_classes")
class ProductShipping(ApiObject):
    ro_attributes = {'id', 'count'}
    rw_attributes = {'name', 'slug', 'description'}

    @classmethod
    def get_product_shipping_classes(cls, api, id='', **params):
        return api.get_product_shipping_classes(id, **params)

    @classmethod
    def create_product_shipping_class(cls, api, **kwargs):
        return api.create_product_shipping_class(**kwargs)

    @classmethod
    def edit_product_shipping_class(cls, api, id, **kwargs):
        return api.update_product_shipping_class(id, **kwargs)

    @classmethod
    def delete_product_shipping_class(cls, api, id):
        return api.delete_product_shipping_class(id)

    def update(self):
        return self._api.update_product_shipping_class(**to_json(self))

    def delete(self):
        return self._api.delete_product_shipping_class(self.id)

    def refresh(self):
        self.__dict__ = self._api.get_product_shipping_classes(id=self.id).__dict__
