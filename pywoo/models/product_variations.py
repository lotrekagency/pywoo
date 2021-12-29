from re import search

from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="variations")
class ProductVariation(ApiObject):
    """
    Class for handling product variation objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-properties>`__
    """
    _ro_attributes = {
        'id', 'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt', 'permalink',
        'price', 'on_sale', 'purchasable', 'backorders_allowed', 'backordered', 'shipping_class_id'
    }
    _rw_attributes = {
        'description', 'sku', 'regular_price', 'sale_price', 'date_on_sale_from',
        'date_on_sale_from_gmt', 'date_on_sale_to', 'date_on_sale_to_gmt', 'virtual',
        'downloadable', 'downloads', 'download_limit', 'download_expiry', 'tax_status', 'tax_class',
        'manage_stock', 'stock_quantity', 'backorders', 'weight', 'dimensions',
        'shipping_class', 'image', 'attributes', 'menu_order', 'meta_data'
    }

    @classmethod
    def get_product_variations(cls, api, product_id, id='', **params):
        """
        Get all or single product variation by id

        :param api: API object
        :type api: pywoo.Api
        :param product_id: Parent Product ID
        :type product_id: int, str
        :param id: If specified gets a single product variation by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more product variations (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-variations>`__)
        :rtype: list of pywoo.models.product_variations.ProductVariation,
            pywoo.models.product_variations.ProductVariation
        """
        return api.get_product_variations(product_id, id, **params)

    @classmethod
    def create_product_variation(cls, api, product_id, **data):
        """
        Create new product variation

        :param api: API object
        :type api: pywoo.Api
        :param product_id: Parent Product ID
        :type product_id: int, str
        :param data: Product variation properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-properties>`__)
        :rtype: pywoo.models.product_variations.ProductVariation
        """
        return api.create_product_variation(product_id, **data)

    @classmethod
    def edit_product_variation(cls, api, product_id, id, **data):
        """
        Change product variation's properties

        :param api: API object
        :type api: pywoo.Api
        :param product_id: Parent Product ID
        :type product_id: int, str
        :param id: Product variation id
        :type id: int, str
        :param data: Product variation properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-properties>`__)
        :rtype: pywoo.models.product_variations.ProductVariation
        """
        return api.update_product_variation(product_id, id, **data)

    @classmethod
    def delete_product_variation(cls, api, product_id, id):
        """
        Delete a product variation by id

        :param api: API object
        :type api: pywoo.Api
        :param product_id: Parent Product ID
        :type product_id: int, str
        :param id: Product variation id
        :type id: int, str
        :rtype: pywoo.models.product_variations.ProductVariation
        """
        return api.delete_product_variation(product_id, id)

    def update(self):
        """
        Push product variation properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.product_variations.ProductVariation.refresh()` method or use the returned object
        which is updated.

        :return: Product variation with updated properties coming from the REST API
        :rtype: pywoo.models.product_variations.ProductVariation
        """
        return self._api.update_product_variation(self.product_id, **to_dict(self))

    def delete(self):
        """
        Delete product variation. The object can't be used anymore after its deletion.

        :return: Deleted product tag
        :rtype: pywoo.models.product_variations.ProductVariation
        """
        return self._api.delete_product_variation(self.product_id, self.id)

    def refresh(self):
        """
        Refresh product variation properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_product_variations(product_id=self.product_id, id=self.id).__dict__

    @property
    def product_id(self):
        return search(r"products\/(\d+)\/.*", self._url).group(1)


@ClassParser(url_class="variations")
class ProductVariationDownload(ApiProperty):
    """
    Class for handling downloads inside :class:`~pywoo.models.product_variations.ProductVariation` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-downloads-properties>`__
    """
    _rw_attributes = {'id', 'name', 'file'}


@ClassParser(url_class="variations")
class ProductVariationDimension(ApiProperty):
    """
    Class for handling dimensions inside :class:`~pywoo.models.product_variations.ProductVariation` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-dimensions-properties>`__
    """
    _rw_attributes = {'lenght', 'width', 'height'}


@ClassParser(url_class="variations")
class ProductImage(ApiProperty):
    """
    Class for handling images inside :class:`~pywoo.models.product_variations.ProductVariation` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-image-properties>`__
    """
    _ro_attributes = {'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt'}
    _rw_attributes = {'id', 'src', 'name', 'alt'}


@ClassParser(url_class="variations")
class ProductVariationAttribute(ApiProperty):
    """
    Class for handling product attributes inside :class:`~pywoo.models.product_variations.ProductVariation` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-attributes-properties>`__
    """
    _rw_attributes = {'id', 'name', 'option'}
