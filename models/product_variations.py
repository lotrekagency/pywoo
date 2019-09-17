from utils.models import ApiObject
from utils.parse import parse_date_time, to_json


class ProductVariation(ApiObject):
    def __init__(self, id, date_created, date_created_gmt, date_modified, date_modified_gmt, description, permalink,
                 sku, price, regular_price, sale_price, date_on_sale_from, date_on_sale_from_gmt, date_on_sale_to,
                 date_on_sale_to_gmt, on_sale, status, purchasable, virtual, downloadable, downloads, download_limit,
                 download_expiry, tax_status, tax_class, manage_stock, stock_quantity, stock_status, backorders,
                 backorders_allowed, backordered, weight, dimensions, shipping_class, shipping_class_id, image,
                 attributes, menu_order, meta_data, api, url):
        super().__init__(api, url)
        self._id = id
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self._date_modified = parse_date_time(date_modified)
        self._date_modified_gmt = parse_date_time(date_modified_gmt)
        self.description = description
        self._permalink = permalink
        self.sku = sku
        self._price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.date_on_sale_from = parse_date_time(date_on_sale_from)
        self.date_on_sale_from_gmt = parse_date_time(date_on_sale_from_gmt)
        self.date_on_sale_to = parse_date_time(date_on_sale_to)
        self.date_on_sale_to_gmt = parse_date_time(date_on_sale_to_gmt)
        self._on_sale = on_sale
        self.status = status
        self._purchasable = purchasable
        self.virtual = virtual
        self.downloadable = downloadable
        self.downloads = downloads
        self.download_limit = download_limit
        self.download_expiry = download_expiry
        self.tax_status = tax_status
        self.tax_class = tax_class
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.stock_status = stock_status
        self.backorders = backorders
        self._backorders_allowed = backorders_allowed
        self._backordered = backordered
        self.weight = weight
        self.dimensions = dimensions
        self.shipping_class = shipping_class
        self._shipping_class_id = shipping_class_id
        self.image = image
        self.attributes = attributes
        self.menu_order = menu_order
        self.meta_data = meta_data

    @classmethod
    def get_product_variations(cls, api, product_id, id='', **params):
        return api.get_product_variations(product_id=product_id, **params)

    @classmethod
    def create_product_variation(cls, api, product_id, **kwargs):
        return api.create_product_variation(product_id=product_id, **kwargs)
    
    @classmethod
    def edit_product_variation(cls, api, product_id, id, **kwargs):
        return api.update_product_variation(product_id=product_id, id=id, **kwargs)

    @classmethod
    def delete_product_variation(cls, api, product_id, id):
        return api.delete_product_variation(product_id=product_id, id=id)

    def update(self):
        return self._api.update_product_variation(self.product_id, self.id, **to_json(self))

    def delete(self):
        return self._api.delete_product_variation(self.product_id, self.id)

    @property
    def id(self):
        return self._id

    @property
    def date_created(self):
        return self._date_created

    @property
    def date_created_gmt(self):
        return self._date_created_gmt

    @property
    def date_modified(self):
        return self._date_modified

    @property
    def date_modified_gmt(self):
        return self._date_modified_gmt

    @property
    def permalink(self):
        return self._permalink

    @property
    def price(self):
        return self._price

    @property
    def on_sale(self):
        return self._on_sale

    @property
    def purchasable(self):
        return self._purchasable

    @property
    def backorders_allowed(self):
        return self._backorders_allowed

    @property
    def backordered(self):
        return self._backordered

    @property
    def shipping_class_id(self):
        return self._shipping_class_id

    @property
    def product_id(self):
        return self._url.split('/')[1]
