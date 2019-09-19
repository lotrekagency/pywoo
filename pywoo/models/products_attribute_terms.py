from re import search

from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_json, ClassParser


@ClassParser()
class ProductAttributeTerm(ApiObject):
    def __init__(self, id, name, slug, description, menu_order, count, api, url):
        super().__init__(api, url)
        self._id = id
        self.name = name
        self.slug = slug
        self.description = description
        self.menu_order = menu_order
        self._count = count

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
        return self._api.update_product_attribute_term(self.product_attribute_id, self.id, **to_json(self))

    def delete(self):
        return self._api.delete_product_attribute_term(self.product_attribute_id, self.id)

    @property
    def id(self):
        return self._id

    @property
    def count(self):
        return self._count

    @property
    def product_attribute_id(self):
        return search(r"products\/attributes\/(\d+)\/.*", self._url).group(1)
