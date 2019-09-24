from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser, to_json


@ClassParser(url=r"products\/shipping_classes.*", url_class="shipping_classes")
class ProductShipping(ApiObject):
    def __init__(self, id, name, slug, description, count, api, url):
        super().__init__(api, url)
        self._id = id
        self.name = name
        self.slug = slug
        self.description = description
        self._count = count

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
        return self._api.update_product_shipping_class(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_product_shipping_class(self.id)
    
    @property
    def id(self):
        return self._id

    @property
    def count(self):
        return self._count
