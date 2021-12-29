from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser, to_dict


@ClassParser(url_class="tags")
class ProductTag(ApiObject):
    """
    Class for handling product tags objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-tags-properties>`__
    """
    _ro_attributes = {'id', 'count'}
    _rw_attributes = {'name', 'slug', 'description'}

    @classmethod
    def get_product_tags(cls, api, id='', **params):
        """
        Get all or single product tags by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a product shipping class by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more product tags (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-tags>`__)
        :rtype: list of pywoo.models.product_tags.ProductTag,
            pywoo.models.product_tags.ProductTag
        """
        return api.get_product_tags(id, **params)

    @classmethod
    def create_product_tag(cls, api, **data):
        """
        Create new product tag

        :param api: API object
        :type api: pywoo.Api
        :param data: Product tag properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-tag-properties>`__)
        :rtype: pywoo.models.product_tags.ProductTag
        """
        return api.create_product_tag(**data)

    @classmethod
    def edit_product_tag(cls, api, id, **data):
        """
        Change product tag's properties

        :param api: API object
        :type api: pywoo.Api
        :param id: Product tag id
        :type id: int, str
        :param data: Product tag properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-tag-properties>`__)
        :rtype: pywoo.models.product_tags.ProductTag
        """
        return api.update_product_tag(id, **data)

    @classmethod
    def delete_product_tag(cls, api, id):
        """
        Delete a product tag by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Product tag id
        :type id: int, str
        :rtype: pywoo.models.product_tags.ProductTag
        """
        return api.delete_product_tag(id)

    def update(self):
        """
        Push product tag properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.product_tags.ProductTag.refresh()` method or use the returned object
        which is updated.

        :return: Product tag with updated properties coming from the REST API
        :rtype: pywoo.models.product_tags.ProductTag
        """
        return self._api.update_product_tag(**to_dict(self))

    def delete(self):
        """
        Delete product tag. The object can't be used anymore after its deletion.

        :return: Deleted product tag
        :rtype: pywoo.models.product_tags.ProductTag
        """
        return self._api.delete_product_tag(self.id)

    def refresh(self):
        """
        Refresh product tag properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_product_tags(id=self.id).__dict__
