from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser


@ClassParser()
class TaxClass(ApiObject):
    def __init__(self, slug, name, api, url):
        super().__init__(api, url)
        self._slug = slug
        self.name = name

    @classmethod
    def get_tax_classes(cls, api):
        return api.get_tax_classes()

    @classmethod
    def create_tax_class(cls, api, **kwargs):
        return api.create_tax_class(**kwargs)

    @classmethod
    def delete_tax_rate(cls, api, slug):
        return api.delete_tax_class(slug)

    def delete(self):
        return self._api.delete_tax_class(self._slug)

    @property
    def slug(self):
        return self._slug
