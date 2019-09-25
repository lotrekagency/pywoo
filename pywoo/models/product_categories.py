from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_json, ClassParser


@ClassParser(url_class="categories")
class ProductCategory(ApiObject):
    ro_attributes = {'id', 'count'}
    rw_attributes = {'name', 'slug', 'parent', 'description', 'display', 'image', 'menu_order'}

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
        return self._api.update_product_category(**to_json(self))

    def delete(self):
        return self._api.delete_product_category(self.id)

    def refresh(self):
        self.__dict__ = self._api.get_product_categories(id=self.id).__dict__


@ClassParser(url_class="categories")
class ProductCategoryImage(ApiProperty):
    ro_attributes = {'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt'}
    rw_attributes = {'id', 'src', 'name', 'alt'}
