from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_json, ClassParser


@ClassParser(url_class="attributes")
class ProductAttribute(ApiObject):
    ro_attributes = {'id'}
    rw_attributes = {'name', 'slug', 'type', 'order_by', 'has_archives'}

    @classmethod
    def get_product_attributes(cls, api, id='', **params):
        return api.get_product_attributes(id, **params)

    @classmethod
    def create_product_attribute(cls, api, **kwargs):
        return api.create_product_attribute(**kwargs)

    @classmethod
    def edit_product_attribute(cls, api, id, **kwargs):
        return api.update_product_attribute(id, **kwargs)

    @classmethod
    def delete_product_attribute(cls, api, id):
        return api.delete_product_attribute(id)

    def update(self):
        return self._api.update_product_attribute(**to_json(self))

    def delete(self):
        return self._api.delete_product_attribute(self.id)
    
    def refresh(self):
        self.__dict__ = self._api.get_product_attributes(id=self.id).__dict__

