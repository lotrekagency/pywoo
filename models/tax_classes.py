from utils.models import ApiObject


class TaxClass(ApiObject):
    def __init__(self, slug, name, api):
        super().__init__(api)
        self._slug = slug
        self.name = name

    def slug(self):
        return self._slug
