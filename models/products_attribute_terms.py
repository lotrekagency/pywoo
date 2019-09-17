from utils.models import ApiObject
from utils.parse import from_json, to_json, parse_date_time



class ProductAttributeTerm(ApiObject):
    def __init__(self, id, name, slug, description, menu_order, count, api):
        super().__init__(api)
        self._id = id
        self.name = name
        self.slug = slug
        self.description = description
        self.menu_order = menu_order
        self._count = count

    @property
    def id(self):
        return self._id

    @property
    def count(self):
        return self._count
