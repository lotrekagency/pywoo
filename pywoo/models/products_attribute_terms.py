from re import search

from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="terms")
class ProductAttributeTerm(ApiObject):
    """
    Class for handling product attribute terms objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-term-properties>`__
    """
    _ro_attributes = {'id', 'count'}
    _rw_attributes = {'name', 'slug', 'description', 'menu_order'}

    @classmethod
    def get_product_attribute_terms(cls, api, product_attribute_id, id='', **params):
        """
        Get all or a single term by id from product attribute

        :param api: API object
        :type api: pywoo.Api
        :param product_attribute_id: Product attribute ID
        :type product_attribute_id: int, str
        :param id: If specified gets a product attribute term by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more product attribute terms (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-attribute-terms>`__)
        :rtype: list of pywoo.models.products_attribute_terms.ProductAttributeTerm,
            pywoo.models.products_attribute_terms.ProductAttributeTerm
        """
        return api.get_product_attribute_terms(product_attribute_id, id, **params)

    @classmethod
    def create_product_attribute_term(cls, api, product_attribute_id, **data):
        """
        Add new term to product attribute

        :param api: API object
        :type api: pywoo.Api
        :param product_attribute_id: Product attribute ID
        :type product_attribute_id: int, str
        :param data: Product attribute term properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-term-properties>`__)
        :rtype: pywoo.models.products_attribute_terms.ProductAttributeTerm
        """
        return api.create_product_attribute_term(product_attribute_id, **data)

    @classmethod
    def edit_product_attribute_term(cls, api, product_attribute_id, id, **data):
        """
        Change product attribute term's properties

        :param api: API object
        :type api: pywoo.Api
        :param product_attribute_id: Product attribute ID
        :type product_attribute_id: int, str
        :param id: Product attribute term id
        :type id: int, str
        :param data: Product attribute term properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-term-properties>`__)
        :rtype: pywoo.models.products_attribute_terms.ProductAttributeTerm
        """
        return api.update_product_attribute_term(product_attribute_id, id, **data)

    @classmethod
    def delete_product_attribute_term(cls, api, product_attribute_id, id):
        """
        Delete product attribute term

        :param api: API object
        :type api: pywoo.Api
        :param product_attribute_id: Product attribute ID
        :type product_attribute_id: int, str
        :param id: Product attribute term id
        :type id: int, str
        :rtype: pywoo.models.products_attribute_terms.ProductAttributeTerm
        """
        return api.delete_product_attribute_term(product_attribute_id, id)

    def update(self):
        """
        Push product attribute term properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.products_attribute_terms.ProductAttributeTerm.refresh()` method or use the returned object
        which is updated.

        :return: Product attribute term with updated properties coming from the REST API
        :rtype: pywoo.models.products_attribute_terms.ProductAttributeTerm
        """
        return self._api.update_product_attribute_term(self.product_attribute_id, **to_dict(self))

    def delete(self):
        """
        Delete product attribute term. The object can't be used anymore after its deletion.

        :return: Deleted product tag
        :rtype: pywoo.models.products_attribute_terms.ProductAttributeTerm
        """
        return self._api.delete_product_attribute_term(self.product_attribute_id, self.id)

    def refresh(self):
        """
        Refresh product attribute term properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_product_attribute_terms(product_attribute_id=self.product_attribute_id, id=self.id).__dict__

    @property
    def product_attribute_id(self):
        return search(r"products\/attributes\/(\d+)\/.*", self._url).group(1)
