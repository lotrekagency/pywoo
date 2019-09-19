from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser, to_json


@ClassParser(url=r"products\/tags.*")
class ProductTag(ApiObject):
    def __init__(self, id, name, slug, description, count, api, url):
        super().__init__(api, url)
        self._id = id
        self.name = name
        self.slug = slug
        self.description = description
        self._count = count

    @classmethod
    def get_product_tags(cls, api, id='', **params):
        return api.get_product_tags(id, **params)

    @classmethod
    def create_product_tag(cls, api, **kwargs):
        return api.create_product_tag(**kwargs)

    @classmethod
    def edit_product_tag(cls, api, id, **kwargs):
        return api.update_product_tag(id, **kwargs)

    @classmethod
    def delete_product_tag(cls, api, id):
        return api.delete_product_tag(id)

    def update(self):
        return self._api.update_product_tag(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_product_tag(self.id)

    @property
    def id(self):
        return self._id

    @property
    def count(self):
        return self._count
