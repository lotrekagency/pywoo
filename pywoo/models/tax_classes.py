from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser


@ClassParser(url_class="classes")
class TaxClass(ApiObject):
    ro_attributes = {'slug'}
    rw_attributes = {'name'}

    @classmethod
    def get_tax_classes(cls, api):
        return api.get_tax_classes()

    @classmethod
    def create_tax_class(cls, api, **kwargs):
        return api.create_tax_class(**kwargs)

    @classmethod
    def delete_tax_class(cls, api, slug):
        return api.delete_tax_class(slug)

    def delete(self):
        return self._api.delete_tax_class(self.slug)
    

