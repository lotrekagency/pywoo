from pywoo.utils.models import ApiObject, ApiProperty, ApiActiveProperty
from pywoo.utils.parse import parse_date_time, to_json, ClassParser


class ProductCategory(ApiActiveProperty):
    rw_attributes = {'id', 'name', 'slug'}

    def get_category(self):
        self._api.get_product_categories(self.id)


class ProductTag(ApiActiveProperty):
    rw_attributes = {'id', 'name', 'slug'}

    def get_tag(self):
        self._api.get_product_tags(self.id)


@ClassParser(url_class="products")
class Product(ApiObject):
    ro_attributes = {'id', 'permalink', 'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt',
                     'price', 'price_html', 'on_sale', 'purchasable', 'total_sales', 'backorders_allowed',
                     'backordered', 'shipping_required', 'shipping_taxable', 'shipping_class_id', 'average_rating',
                     'rating_count', 'related_ids', 'variations'}
    rw_attributes = {'name', 'slug', 'type', 'status', 'featured', 'catalog_visibility', 'description',
                     'short_description', 'sku', 'regular_price', 'sale_price', 'date_on_sale_from',
                     'date_on_sale_from_gmt', 'date_on_sale_to', 'date_on_sale_to_gmt', 'virtual', 'downloadable',
                     'downloads', 'download_limit', 'download_expiry', 'external_url', 'button_text', 'tax_status',
                     'tax_class', 'manage_stock', 'stock_quantity', 'stock_status', 'backorders', 'sold_individually',
                     'weight', 'dimensions', 'shipping_class', 'reviews_allowed', 'upsell_ids', 'cross_sell_ids',
                     'parent_id', 'purchase_note', 'categories', 'tags', 'images', 'attributes', 'default_attributes',
                     'grouped_products', 'menu_order', 'meta_data'}

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
        return api.get_products(id, **params)

    @classmethod
    def create_product(cls, api, **kwargs):
        return api.create_product(**kwargs)

    @classmethod
    def edit_product(cls, api, id, **kwargs):
        return api.update_product(id, **kwargs)

    @classmethod
    def delete_product(cls, api, id, **params):
        return api.delete_product(id, **params)

    def update(self):
        return self._api.update_product(**to_json(self))

    def delete(self):
        return self._api.delete_product(self.id)
    
    def refresh(self):
        self.__dict__ = self._api.get_products(id=self.id).__dict__


@ClassParser(url_class="products")
class ProductDownload(ApiProperty):
    rw_attributes = {'id', 'name', 'file'}


@ClassParser(url_class="products")
class ProductDimension(ApiProperty):
    rw_attributes = {'lenght', 'width', 'height'}


@ClassParser(url_class="products")
class ProductImage(ApiProperty):
    ro_attributes = {'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt'}
    rw_attributes = {'id', 'src', 'name', 'alt'}


@ClassParser(url_class="products")
class ProductAttribute(ApiActiveProperty):
    rw_attributes = {'id', 'name', 'position', 'visible', 'variation', 'options'}

    def get_product_attribute(self):
        if self.id == 0:
            return None
        return self._api.get_product_attributes(self.id)


@ClassParser(url_class="products")
class ProductDefaultAttribute(ApiActiveProperty):
    rw_attributes = {'id', 'name', 'option'}

    def get_product_attribute(self):
        if self.id == 0:
            return None
        return self._api.get_product_attributes(self.id)
