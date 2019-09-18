from utils.models import ApiObject
from utils.parse import to_json, ClassParser


@ClassParser()
class ProductCategory(ApiObject):
    def __init__(self, id, name, slug, parent, description, display, image, menu_order, count, api, url):
        super().__init__(api, url)
        self._id = id
        self.name = name
        self.slug = slug
        self.parent = parent
        self.description = description
        self.display = display
        self.image = image
        self.menu_order = menu_order
        self._count = count

    @classmethod
    def get_product_categories(cls, api, id='', **params):
        return api.get_product_categories(id, **params)

    @classmethod
    def create_product_category(cls, api, **kwargs):
        return api.create_product_category(**kwargs)

    @classmethod
    def edit_product_category(cls, api, id, **kwargs):
        return api.update_product_category(id, **kwargs)

    @classmethod
    def delete_product_category(cls, api, id):
        return api.delete_product_category(id)

    def update(self):
        return self._api.update_product_category(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_product_category(self.id)

    @property
    def id(self):
        return self._id

    @property
    def count(self):
        return self._count
