from utils.models import ApiObject


class ProductShippingTag(ApiObject):
    def __init__(self, id, name, slug, description, count, api):
        super().__init__(api)
        self._id = id
        self.name = name
        self.slug = slug
        self.description = description
        self._count = count

    @property
    def id(self):
        return self._id

    @property
    def count(self):
        return self._count
