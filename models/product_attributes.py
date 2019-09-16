from utils.models import ApiObject


class ProductAttribute(ApiObject):
    def __init__(self, id, name, slug, type, order_by, has_archives, api):
        super().__init__(api)
        self._id = id
        self.name = name
        self.slug = slug
        self.type = type
        self.order_by = order_by
        self.has_archives = has_archives

    @property
    def id(self):
        return self._id
