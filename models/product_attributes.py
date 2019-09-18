from utils.models import ApiObject
from utils.parse import to_json


class ProductAttribute(ApiObject):
    def __init__(self, id, name, slug, type, order_by, has_archives, api, url):
        super().__init__(api, url)
        self._id = id
        self.name = name
        self.slug = slug
        self.type = type
        self.order_by = order_by
        self.has_archives = has_archives

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
        return self._api.update_product_attribute(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_product_attribute(self.id)

    @property
    def id(self):
        return self._id
