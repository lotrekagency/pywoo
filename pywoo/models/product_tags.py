from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser, to_json


@ClassParser(url_class="tags")
class ProductTag(ApiObject):
    ro_attributes = {'id', 'count'}
    rw_attributes = {'name', 'slug', 'description'}

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
        return self._api.update_product_tag(**to_json(self))

    def delete(self):
        return self._api.delete_product_tag(self.id)
    
    def refresh(self):
        self.__dict__ = self._api.get_product_tags(id=self.id).__dict__

