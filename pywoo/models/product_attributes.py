from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="attributes")
class ProductAttribute(ApiObject):
    """
    Class for handling product attribute objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-properties>`__
    """
    _ro_attributes = {'id'}
    _rw_attributes = {'name', 'slug', 'type', 'order_by', 'has_archives'}

    @classmethod
    def get_product_attributes(cls, api, id='', **params):
        """
        Get all or single product attribute by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a product attribute by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of product attributes (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-attributes>`__)
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return api.get_product_attributes(id, **params)

    @classmethod
    def create_product_attribute(cls, api, **data):
        """
        Create product attribute

        :param api: API object
        :type api: pywoo.Api
        :param data: Product attribute properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-properties>`__)
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return api.create_product_attribute(**data)

    @classmethod
    def edit_product_attribute(cls, api, id, **data):
        """
        Change product attribute's properties by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Product attribute id
        :type id: int, str
        :param data: Product attribute properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-properties>`__)
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return api.update_product_attribute(id, **data)

    @classmethod
    def delete_product_attribute(cls, api, id):
        """
        Delete product attribute by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Product attribute id
        :type id: int, str
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return api.delete_product_attribute(id)

    def update(self):
        """
        Push product attribute properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.product_attributes.ProductAttribute.refresh()` method or use the returned object
        which is updated.

        :return: Product attribute with updated properties coming from the REST API
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return self._api.update_product_attribute(**to_dict(self))

    def delete(self):
        """
        Delete product attribute. The object can't be used anymore after its deletion.

        :return: Deleted product attribute
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return self._api.delete_product_attribute(self.id)

    def refresh(self):
        """
        Refresh product attribute properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_product_attributes(id=self.id).__dict__
