from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser, to_dict


@ClassParser(url_class="shipping_classes")
class ProductShipping(ApiObject):
    """
    Class for handling product shipping objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-shipping-class-properties>`__
    """
    _ro_attributes = {'id', 'count'}
    _rw_attributes = {'name', 'slug', 'description'}

    @classmethod
    def get_product_shipping_classes(cls, api, id='', **params):
        """
        Get all or single product shipping class by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a product shipping class by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more product shipping classes (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-shipping-classes>`__)
        :rtype: list of pywoo.models.product_shipping_classes.ProductShipping,
            pywoo.models.product_shipping_classes.ProductShipping
        """
        return api.get_product_shipping_classes(id, **params)

    @classmethod
    def create_product_shipping_class(cls, api, **data):
        """
        Create new product shipping class

        :param api: API object
        :type api: pywoo.Api
        :param data: Product shipping class properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-shipping-class-properties>`__)
        :rtype: pywoo.models.product_shipping_classes.ProductShipping
        """
        return api.create_product_shipping_class(**data)

    @classmethod
    def edit_product_shipping_class(cls, api, id, **data):
        """
        Change product shipping class' properties

        :param api: API object
        :type api: pywoo.Api
        :param id: Product shipping class id
        :type id: int, str
        :param data: Product shipping class properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-shipping-class-properties>`__)
        :rtype: pywoo.models.product_shipping_classes.ProductShipping
        """
        return api.update_product_shipping_class(id, **data)

    @classmethod
    def delete_product_shipping_class(cls, api, id):
        """
        Delete product shipping class

        :param api: API object
        :type api: pywoo.Api
        :param id: Product shipping class id
        :type id: int,str
        :rtype: pywoo.models.product_shipping_classes.ProductShipping
        """
        return api.delete_product_shipping_class(id)

    def update(self):
        """
        Push product shipping properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.product_shipping_classes.ProductShipping.refresh()` method or use the returned object
        which is updated.

        :return: Product shipping with updated properties coming from the REST API
        :rtype: pywoo.models.product_shipping_classes.ProductShipping
        """
        return self._api.update_product_shipping_class(**to_dict(self))

    def delete(self):
        """
        Delete product shipping. The object can't be used anymore after its deletion.

        :return: Deleted product shipping
        :rtype: pywoo.models.product_shipping_classes.ProductShipping
        """
        return self._api.delete_product_shipping_class(self.id)

    def refresh(self):
        """
        Refresh product shipping properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_product_shipping_classes(id=self.id).__dict__
