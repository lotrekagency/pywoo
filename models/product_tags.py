from utils.models import ApiObject
from utils.parse import ClassParser


@ClassParser(url=r"products\/tags.*")
class ProductTag(ApiObject):
    def __init__(self, id, name, slug, description, count, api, url):
        super().__init__(api, url)
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
