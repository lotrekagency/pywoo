from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="categories")
class ProductCategory(ApiObject):
    """
    Class for handling product category objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-category-properties>`__
    """
    _ro_attributes = {'id', 'count'}
    _rw_attributes = {'name', 'slug', 'parent', 'description', 'display', 'image', 'menu_order'}

    @classmethod
    def get_product_categories(cls, api, id='', **params):
        """
        Get all or a single product category by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a product category by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of product category (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-categories>`__)
        :rtype: list of pywoo.models.product_categories.ProductCategory, pywoo.models.product_categories.ProductCategory
        """
        return api.get_product_categories(id, **params)

    @classmethod
    def create_product_category(cls, api, **data):
        """
        Create new product category

        :param api: API object
        :type api: pywoo.Api
        :param data: Product category properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-category-properties>`__)
        :rtype: pywoo.models.product_categories.ProductCategory
        """
        return api.create_product_category(**data)

    @classmethod
    def edit_product_category(cls, api, id, **data):
        """
        Change product category's properties

        :param api: API object
        :type api: pywoo.Api
        :param id: Product category id
        :type id: int, str
        :param data: Product category properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-category-properties>`__)
        :rtype: pywoo.models.product_categories.ProductCategory
        """
        return api.update_product_category(id, **data)

    @classmethod
    def delete_product_category(cls, api, id):
        """
        Delete product category by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Product category id
        :type id: int, str
        :rtype: pywoo.models.product_categories.ProductCategory
        """
        return api.delete_product_category(id)

    def update(self):
        """
        Push product category properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.product_categories.ProductCategory.refresh()` method or use the returned object
        which is updated.

        :return: Product category with updated properties coming from the REST API
        :rtype: pywoo.models.product_categories.ProductCategory
        """
        return self._api.update_product_category(**to_dict(self))

    def delete(self):
        """
        Delete product category. The object can't be used anymore after its deletion.

        :return: Deleted product category
        :rtype: pywoo.models.product_categories.ProductCategory
        """
        return self._api.delete_product_category(self.id)

    def refresh(self):
        """
        Refresh product category properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_product_categories(id=self.id).__dict__


@ClassParser(url_class="categories")
class ProductCategoryImage(ApiProperty):
    """
    Class for handling product category image properties
    inside :class:`~pywoo.models.product_categories.ProductCategory` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-category-image-properties>`__
    """
    _ro_attributes = {'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt'}
    _rw_attributes = {'id', 'src', 'name', 'alt'}
