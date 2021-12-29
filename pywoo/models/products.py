from pywoo.utils.models import ApiObject, ApiProperty, ApiActiveProperty
from pywoo.utils.parse import to_dict, ClassParser


class ProductCategory(ApiActiveProperty):
    """
    Class for handling product categories inside :class:`~pywoo.models.products.Product` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-categories-properties>`__
    """
    _rw_attributes = {'id', 'name', 'slug'}

    def get_category(self):
        """
        Get associated product category object from API

        :rtype: pywoo.models.product_categories.ProductCategory
        """
        self._api.get_product_categories(self.id)


class ProductTag(ApiActiveProperty):
    """
    Class for handling product tags inside :class:`~pywoo.models.products.Product` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-tags-properties>`__
    """
    _rw_attributes = {'id', 'name', 'slug'}

    def get_tag(self):
        """
        Get associated product tag object from API

        :rtype: pywoo.models.product_tags.ProductTag
        """
        self._api.get_product_tags(self.id)


@ClassParser(url_class="products")
class Product(ApiObject):
    """
    Class for handling product objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-tags-properties>`__
    """
    _ro_attributes = {
        'id', 'permalink', 'price', 'price_html', 'on_sale', 'purchasable', 'total_sales',
        'backorders_allowed', 'backordered', 'shipping_required', 'shipping_taxable',
        'shipping_class_id', 'average_rating', 'rating_count', 'related_ids', 'variations'
    }
    _rw_attributes = {
        'name', 'slug', 'type', 'status', 'featured', 'catalog_visibility', 'description',
        'short_description', 'sku', 'regular_price', 'sale_price', 'virtual', 'downloadable',
        'downloads', 'download_limit', 'download_expiry', 'external_url', 'button_text', 'tax_status',
        'tax_class', 'manage_stock', 'stock_quantity', 'backorders', 'sold_individually',
        'weight', 'dimensions', 'shipping_class', 'reviews_allowed', 'upsell_ids', 'cross_sell_ids',
        'parent_id', 'purchase_note', 'categories', 'tags', 'images', 'attributes', 'default_attributes',
        'grouped_products', 'menu_order'
    }

    # noinspection PyArgumentList
    def __init__(self, api, url, **kwargs):
        super().__init__(api, url, **kwargs)
        categories = []
        tags = []
        for cat in self.categories:
            categories.append(ProductCategory(api, **cat))
        for tag in self.tags:
            tags.append(ProductTag(api, **tag))
        self.categories = categories
        self.tags = tags

    @classmethod
    def get_products(cls, api, id='', **params):
        """
        Get all or a single product by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a product by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more products (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-products>`__)
        :rtype: list of pywoo.models.products.Product,
            pywoo.models.products.Product
        """
        return api.get_products(id, **params)

    @classmethod
    def create_product(cls, api, **data):
        """
        Creates a new product

        :param api: API object
        :type api: pywoo.Api
        :param data: Product properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-properties>`__)
        :rtype: pywoo.models.products.Product
        """
        return api.create_product(**data)

    @classmethod
    def edit_product(cls, api, id, **data):
        """
        Change product's properties

        :param api: API object
        :type api: pywoo.Api
        :param id: Product id
        :type id: int, str
        :param data: Product properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-properties>`__)
        :rtype: pywoo.models.products.Product
        """
        return api.update_product(id, **data)

    @classmethod
    def delete_product(cls, api, id, **params):
        """
        Delete a product by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Product id
        :type id: int, str
        :param params: Delete parameters (`Full list of parameters
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#delete-a-product>`__)
        :rtype: pywoo.models.products.Products
        """
        return api.delete_product(id, **params)

    def update(self):
        """
        Push product properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.products.Product.refresh()` method or use the returned object
        which is updated.

        :return: Product with updated properties coming from the REST API
        :rtype: pywoo.models.products.Product
        """
        return self._api.update_product(**to_dict(self))

    def delete(self, force=True):
        """
        Deletes product. The object can't be used anymore after its deletion.

        :param force: Whether to permanently delete product or not
        :type force: bool
        :return: Deleted product
        :rtype: pywoo.models.products.Product
        """
        return self._api.delete_product(self.id, force)

    def refresh(self):
        """
        Refresh product properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_products(id=self.id).__dict__


@ClassParser(url_class="products")
class ProductDownload(ApiProperty):
    """
    Class for handling downloads inside :class:`~pywoo.models.products.Product` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-downloads-properties>`__
    """
    _rw_attributes = {'id', 'name', 'file'}


@ClassParser(url_class="products")
class ProductDimension(ApiProperty):
    """
    Class for handling dimensions inside :class:`~pywoo.models.products.Product` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-dimensions-properties>`__
    """
    _rw_attributes = {'length', 'width', 'height'}


@ClassParser(url_class="products")
class ProductImage(ApiProperty):
    """
    Class for handling images inside :class:`~pywoo.models.products.Product` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-images-properties>`__
    """
    _ro_attributes = {'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt'}
    _rw_attributes = {'id', 'src', 'name', 'alt'}


@ClassParser(url_class="products")
class ProductAttribute(ApiActiveProperty):
    """
    Class for handling product attributes inside :class:`~pywoo.models.products.Product` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attributes-properties>`__
    """
    _rw_attributes = {'id', 'name', 'position', 'visible', 'variation', 'options'}

    def get_product_attribute(self):
        """
        Get associated product attribute object from API

        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        if self.id == 0:
            return None
        return self._api.get_product_attributes(self.id)


@ClassParser(url_class="products")
class ProductDefaultAttribute(ApiActiveProperty):
    """
    Class for handling product default variation attributes inside :class:`~pywoo.models.products.Product` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-default-attributes-properties>`__
    """
    _rw_attributes = {'id', 'name', 'option'}

    def get_product_attribute(self):
        """
        Get associated product attribute object from API

        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        if self.id == 0:
            return None
        return self._api.get_product_attributes(self.id)
