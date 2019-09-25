from re import search

from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import parse_date_time, to_json, ClassParser


@ClassParser(url_class="variations")
class ProductVariation(ApiObject):
    ro_attributes = {'id', 'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt', 'permalink',
                     'price', 'on_sale', 'purchasable', 'backorders_allowed', 'backordered', 'shipping_class_id'}
    rw_attributes = {'description', 'sku', 'regular_price', 'sale_price', 'date_on_sale_from',
                     'date_on_sale_from_gmt', 'date_on_sale_to', 'date_on_sale_to_gmt', 'status', 'virtual',
                     'downloadable', 'downloads', 'download_limit', 'download_expiry', 'tax_status', 'tax_class',
                     'manage_stock', 'stock_quantity', 'stock_status', 'backorders', 'weight', 'dimensions',
                     'shipping_class', 'image', 'attributes', 'menu_order', 'meta_data'}

    @classmethod
    def get_product_variations(cls, api, product_id, id='', **params):
        return api.get_product_variations(product_id, id, **params)

    @classmethod
    def create_product_variation(cls, api, product_id, **kwargs):
        return api.create_product_variation(product_id, **kwargs)

    @classmethod
    def edit_product_variation(cls, api, product_id, id, **kwargs):
        return api.update_product_variation(product_id, id, **kwargs)

    @classmethod
    def delete_product_variation(cls, api, product_id, id):
        return api.delete_product_variation(product_id, id)

    def update(self):
        return self._api.update_product_variation(self.product_id, **to_json(self))

    def delete(self):
        return self._api.delete_product_variation(self.product_id, self.id)
    
    def refresh(self):
        self.__dict__ = self._api.get_product_variations(product_id=self.product_id, id=self.id).__dict__

    @property
    def product_id(self):
        return search(r"products\/(\d+)\/.*", self._url).group(1)


@ClassParser(url_class="variations")
class ProductVariationDownload(ApiProperty):
    rw_attributes = {'id', 'name', 'file'}


@ClassParser(url_class="variations")
class ProductVariationDimension(ApiProperty):
    rw_attributes = {'lenght', 'width', 'height'}


@ClassParser(url_class="variations")
class ProductImage(ApiProperty):
    ro_attributes = {'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt'}
    rw_attributes = {'id', 'src', 'name', 'alt'}


@ClassParser(url_class="variations")
class ProductVariationAttribute(ApiProperty):
    rw_attributes = {'id', 'name', 'option'}
