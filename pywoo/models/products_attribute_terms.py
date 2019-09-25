from re import search

from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_json, ClassParser


@ClassParser(url_class="terms")
class ProductAttributeTerm(ApiObject):
    ro_attributes = {'id', 'count'}
    rw_attributes = {'name', 'slug', 'description', 'menu_order'}

    @classmethod
    def get_product_attribute_terms(cls, api, product_attribute_id, id='', **params):
        return api.get_product_attribute_terms(product_attribute_id, id, **params)

    @classmethod
    def create_product_attribute_term(cls, api, product_attribute_id, **kwargs):
        return api.create_product_attribute_term(product_attribute_id, **kwargs)

    @classmethod
    def edit_product_attribute_term(cls, api, product_attribute_id, id, **kwargs):
        return api.update_product_attribute_term(product_attribute_id, id, **kwargs)

    @classmethod
    def delete_product_attribute_term(cls, api, product_attribute_id, id):
        return api.delete_product_attribute_term(product_attribute_id, id)

    def update(self):
        return self._api.update_product_attribute_term(self.product_attribute_id, **to_json(self))

    def delete(self):
        return self._api.delete_product_attribute_term(self.product_attribute_id, self.id)

    def refresh(self):
        self.__dict__ = self._api.get_product_attribute_terms(product_attribute_id=self.product_attribute_id, id=self.id).__dict__

    @property
    def product_attribute_id(self):
        return search(r"products\/attributes\/(\d+)\/.*", self._url).group(1)
