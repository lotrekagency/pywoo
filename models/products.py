from utils.models import ApiObject
from utils.parse import parse_date_time


class Product(ApiObject):
    def __init__(self, id, name, slug, permalink, date_created, date_created_gmt, date_modified, date_modified_gmt,
                 type, status, featured, catalog_visibility, description, short_description, sku, price, regular_price,
                 sale_price, date_on_sale_from, date_on_sale_from_gmt, date_on_sale_to, date_on_sale_to_gmt, price_html,
                 on_sale, purchasable, total_sales, virtual, downloadable, downloads, download_limit, download_expiry,
                 external_url, button_text, tax_status, tax_class, manage_stock, stock_quantity, stock_status,
                 backorders, backorders_allowed, backordered, sold_individually, weight, dimensions, shipping_required,
                 shipping_taxable, shipping_class, shipping_class_id, reviews_allowed, average_rating, rating_count,
                 related_ids, upsell_ids, cross_sell_ids, parent_id, purchase_note, categories, tags, images,
                 attributes, default_attributes, variations, grouped_products, menu_order, meta_data, api):
        super().__init__(api)
        self._id = id
        self.name = name
        self.slug = slug
        self._permalink = permalink
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self._date_modified = parse_date_time(date_modified)
        self._date_modified_gmt = parse_date_time(date_modified_gmt)
        self.type = type
        self.status = status
        self.featured = featured
        self.catalog_visibility = catalog_visibility
        self.description = description
        self.short_description = short_description
        self.sku = sku
        self._price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.date_on_sale_from = parse_date_time(date_on_sale_from)
        self.date_on_sale_from_gmt = parse_date_time(date_on_sale_from_gmt)
        self.date_on_sale_to = parse_date_time(date_on_sale_to)
        self.date_on_sale_to_gmt = parse_date_time(date_on_sale_to_gmt)
        self._price_html = price_html
        self._on_sale = on_sale
        self._purchasable = purchasable
        self._total_sales = total_sales
        self.virtual = virtual
        self.downloadable = downloadable
        self.downloads = downloads
        self.download_limit = download_limit
        self.download_expiry = download_expiry
        self.external_url = external_url
        self.button_text = button_text
        self.tax_status = tax_status
        self.tax_class = tax_class
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.stock_status = stock_status
        self.backorders = backorders
        self._backorders_allowed = backorders_allowed
        self._backordered = backordered
        self.sold_individually = sold_individually
        self.weight = weight
        self.dimensions = dimensions
        self._shipping_required = shipping_required
        self._shipping_taxable = shipping_taxable
        self.shipping_class = shipping_class
        self._shipping_class_id = shipping_class_id
        self.reviews_allowed = reviews_allowed
        self._average_rating = average_rating
        self._rating_count = rating_count
        self._related_ids = related_ids
        self.upsell_ids = upsell_ids
        self.cross_sell_ids = cross_sell_ids
        self.parent_id = parent_id
        self.purchase_note = purchase_note
        self.categories = categories
        self.tags = tags
        self.images = images
        self.attributes = attributes
        self.default_attributes = default_attributes
        self._variations = variations
        self.grouped_products = grouped_products
        self.menu_order = menu_order
        self.meta_data = meta_data

    @property
    def id(self):
        return self._id

    @property
    def permalink(self):
        return self._permalink

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
    def price(self):
        return self._price

    @property
    def price_html(self):
        return self._price_html

    @property
    def on_sale(self):
        return self._on_sale

    @property
    def purchasable(self):
        return self._purchasable

    @property
    def total_sales(self):
        return self._total_sales

    @property
    def backorders_allowed(self):
        return self._backorders_allowed

    @property
    def backordered(self):
        return self._backordered

    @property
    def shipping_required(self):
        return self._shipping_required

    @property
    def shipping_taxable(self):
        return self._shipping_taxable

    @property
    def shipping_class_id(self):
        return self._shipping_class_id

    @property
    def average_rating(self):
        return self._average_rating

    @property
    def rating_count(self):
        return self._rating_count

    @property
    def related_ids(self):
        return self._related_ids

    @property
    def variations(self):
        return self._variations


class ProductDownload:
    def __init__(self, id=None, name=None, file=None):
        self.id = id
        self.name = name
        self.file = file


class ProductDimension:
    def __init__(self, length=None, width=None, height=None):
        self.length = length
        self.width = width
        self.height = height


class ProductCategory:
    def __init__(self, id=None, name=None, slug=None):
        self.id = id
        self._name = name
        self._slug = slug

    @property
    def name(self):
        return self._name

    @property
    def slug(self):
        return self._slug


class ProductTag:
    def __init__(self, id=None, date_created=None, date_created_gmt=None, date_modified=None, date_modified_gmt=None,
                 src=None, name=None, alt=None):
        self.id = id
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self._date_modified = parse_date_time(date_modified)
        self._date_modified_gmt = parse_date_time(date_modified_gmt)
        self.src = src
        self.name = name
        self.alt = alt

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


class ProductAttribute:
    def __init__(self, id=None, name=None, position=None, visible=None, variation=None, options=[]):
        self.id = id
        self.name = name
        self.position = position
        self.visible = visible
        self.variation = variation
        self.options = options


class ProductDefaultAttribute:
    def __init__(self, id=None, name=None, option=None):
        self.id = id
        self.name = name
        self.option = option
