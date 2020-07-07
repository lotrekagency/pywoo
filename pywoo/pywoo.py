import requests

from requests_oauthlib import OAuth1
from pywoo.models import * # NOQA
from pywoo.utils.parse import from_json
from pywoo.utils.auth import auth_params


class Api:
    """
    Main client class used for sending all the requests to Woocommerce REST API. Even model objects pass from this
    class for doing requests.
    """
    def __init__(self, url, consumer_key, consumer_secret, console_logs=False):
        """
        :param url: URL to Woocommerce REST API (e.g. ``https://example.example/wp-json/wc/v3``)
        :type url: str
        :param consumer_key: Consumer Key
        :type consumer_key: str
        :param consumer_secret: Consumer Secret
        :type consumer_secret: str
        :param console_logs: Whether or not display logs of requests on console
        :type console_logs: bool
        """
        self.url = url
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.console_logs = console_logs

    def _get_default_headers(self):
        headers = {}
        return headers

    def _get_auth_params(self):
        return {
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret
        } if auth_params.get(self.url.split('/')[-1], None) else {}

    def _create(self, url, data):
        resp = requests.post(
            f'{self.url}/{url}',
            json=data,
            headers=self._get_default_headers(),
            params=self._get_auth_params(),
            auth=OAuth1(self.consumer_key, self.consumer_secret, '', '')
        )
        if not resp.ok:
            raise Exception(f"\033[1;31;40mHTTP ERROR {resp.status_code} {resp.json()['message']}\033[0m")
        if self.console_logs:
            print("\033[1;32;40m[Pywoo] STATUS 200 Created successfully\033[0m")
        return from_json(resp.text, self, url)

    def _get(self, url, id='', params={}):
        resp = requests.get(
            f'{self.url}/{url}/{id}',
            params={**params, **self._get_auth_params()},
            auth=OAuth1(self.consumer_key, self.consumer_secret, '', '')
        )
        if not resp.ok:
            raise Exception(f"\033[1;31;40mHTTP ERROR {resp.status_code} {resp.json()['message']}\033[0m")
        if self.console_logs:
            print("\033[1;32;40m[Pywoo] STATUS 200 Read successfully\033[0m")
        return from_json(resp.text, self, url)

    def _put(self, url, id, data):
        resp = requests.put(
            f'{self.url}/{url}/{id}',
            json=data,
            params=self._get_auth_params(),
            auth=OAuth1(self.consumer_key, self.consumer_secret, '', '')
        )
        if not resp.ok:
            raise Exception(f"\033[1;31;40mHTTP ERROR {resp.status_code} {resp.json()['message']}\033[0m")
        if self.console_logs:
            print("\033[1;32;40m[Pywoo] STATUS 200 Updated successfully\033[0m")
        return from_json(resp.text, self, url)

    def _delete(self, url, id, params={}):
        resp = requests.delete(
            f'{self.url}/{url}/{id}',
            headers=self._get_default_headers(),
            params={**params, **self._get_auth_params()},
            auth=OAuth1(self.consumer_key, self.consumer_secret, '', '')
        )
        if not resp.ok:
            raise Exception(f"\033[1;31;40mHTTP ERROR {resp.status_code} {resp.json()['message']}\033[0m")
        if self.console_logs:
            print("\033[1;32;40m[Pywoo] STATUS 200 Deleted successfully\033[0m")
        return from_json(resp.text, self, url)

    def create_coupon(self, **data):
        """
        Create a new coupon

        :param data: Properties for creating a new coupon code (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#coupon-properties>`__)
        :rtype: pywoo.models.coupon.Coupon
        """
        return self._create('coupons', data)

    def get_coupons(self, id='', **params):
        """
        Get all coupon codes or a single coupon code by id

        :param id: If specified gets a single coupon code by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of coupon codes (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-coupons>`__)
        :rtype: list of pywoo.models.coupon.Coupon, pywoo.models.coupon.Coupon
        """
        return self._get('coupons', id, params)

    def update_coupon(self, id, **data):
        """
        Update coupon code properties by id

        :param id: Coupon code id
        :type id: int, str
        :param data: Properties to update (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#coupon-properties>`__)
        :rtype: pywoo.models.coupon.Coupon
        """
        return self._put('coupons', id, data)

    def delete_coupon(self, id, force=True):
        """
        Delete coupon code by id

        :param id: Coupon code id
        :type id: int, str
        :param force: Whether to permanently delete coupon or not
        :type force: bool
        :rtype: pywoo.models.coupon.Coupon
        """
        return self._delete('coupons', id, {'force': force})

    def create_customer(self, **data):
        """
        Create a new customer

        :param data: Properties for creating a new customer (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#customer-properties>`__)
        :rtype: pywoo.models.customers.Customer
        """
        return self._create('customers', data)

    def get_customers(self, id='', **params):
        """
        Get all customers of a single customer by id

        :param id: If specified gets a single customer by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of customers (`Full list of parameters
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-customers>`__)
        :rtype: list of pywoo.models.customers.Customer, pywoo.models.customers.Customer
        """
        return self._get('customers', id, params)

    def update_customer(self, id, **data):
        """
        Update customer's properties by id

        :param id: Customer id
        :type id: int, str
        :param data: Properties to update (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#customer-properties>`__)
        :rtype: pywoo.models.customers.Customer
        """
        return self._put('customers', id, data)

    def delete_customer(self, id, **params):
        """
        Delete customer by id

        :param id: Customer id
        :type id: int, str
        :param params: Additional parameters for deletion (`Full list of parameters
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#delete-a-customer>`__)
        :rtype: pywoo.models.customers.Customer
        """
        params['force'] = True
        return self._delete('customers', id, params)

    def create_order(self, **data):
        """
        Create new order

        :param data: Properties for creating a new order (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-properties>`__)
        :rtype: pywoo.models.orders.Order
        """
        return self._create('orders', data)

    def get_orders(self, id='', **params):
        """
        Get all orders or a single order by id

        :param id: If specified gets a single order by id
        :type id: int, str
        :param params: Parameters that can be used when retrieving order(s);
            list of parameters:
             - `Single order <https://woocommerce.github.io/woocommerce-rest-api-docs/#retrieve-an-order>`_
             - `List of orders <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-orders>`_
        :rtype: list of pywoo.models.orders.Order, pywoo.models.orders.Order
        """
        return self._get('orders', id, params)

    def update_order(self, id, **data):
        """
        Update order properties by id

        :param id: Order id
        :type id: int, str
        :param data: Properties to update (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-properties>`__)
        :rtype: pywoo.models.orders.Order
        """
        return self._put('orders', id, data)

    def delete_order(self, id, force=True):
        """
        Delete order by id

        :param id: Order id
        :type id: int, str
        :param force: Whether to permanently delete order or not
        :type force: bool
        :rtype: pywoo.models.orders.Order
        """
        return self._delete('orders', id, {'force': force})

    def create_order_note(self, order_id, **data):
        """
        Add new note to order

        :param order_id: Order id
        :type order_id: int, str
        :param data: Order note properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-note-properties>`__)
        :rtype: pywoo.models.order_notes.OrderNote
        """
        return self._create(f'orders/{order_id}/notes', data)

    def get_order_notes(self, order_id, id='', **params):
        """
        Get all notes or single note from order

        :param order_id: Order id
        :type order_id: int, str
        :param id: If specified gets a order note by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of order notes (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-order-notes>`__)
        :rtype: list of pywoo.models.order_notes.OrderNote, pywoo.models.order_notes.OrderNote
        """
        return self._get(f'orders/{order_id}/notes', id, params)

    def delete_order_note(self, order_id, id):
        """
        Delete note from order

        :param order_id: Order id
        :type order_id: int, str
        :param id: Order note id
        :type id: int, str
        :rtype: pywoo.models.order_notes.OrderNote
        """
        return self._delete(f'orders/{order_id}/notes', id, {'force': True})

    def create_refund(self, order_id, **data):
        """
        Create refund by order

        :param order_id: Order id
        :type order_id: int, str
        :param data: Refund properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-refund-properties>`__)
        :rtype: pywoo.models.refunds.Refund
        """
        return self._create(f'orders/{order_id}/refunds', data)

    def get_refunds(self, order_id, id='', **params):
        """
        Get refunds or single refund from order

        :param order_id: Order id
        :type order_id: int, str
        :param id: If specified gets a refund by id
        :type id: int, str
        :param params: Parameters that can be used when retrieving refund(s);
            list of parameters:
             - `Single refund <https://woocommerce.github.io/woocommerce-rest-api-docs/#retrieve-a-refund>`__
             - `List of refunds <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-refunds>`__
        :rtype: list of pywoo.models.refunds.Refund, pywoo.models.refunds.Refund
        """
        return self._get(f'orders/{order_id}/refunds', id, params)

    def update_refund(self, order_id, id, **data):
        """
        Update refund from order

        :param order_id: Order id
        :type order_id: int, str
        :param id: Refund id
        :type id: int, str
        :param data: Refund properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-refund-properties>`__)
        :rtype: pywoo.models.refunds.Refund
        """
        return self._put(f'orders/{order_id}/refunds', id, data)

    def delete_refund(self, order_id, id):
        """
        Delete refund from order

        :param order_id: Order id
        :type order_id: int, str
        :param id: Refund id
        :type id: int, str
        :rtype: pywoo.models.refunds.Refund
        """
        return self._delete(f'orders/{order_id}/refunds', id, {'force': True})

    def create_product(self, **data):
        """
        Create new product

        :param data: Product properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-properties>`__)
        :rtype: pywoo.models.products.Product
        """
        return self._create('products', data)

    def get_products(self, id='', **params):
        """
        Get all products or a single product by id

        :param id: If specified gets a product by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of products (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-products>`__)
        :rtype: list of pywoo.models.products.Product, pywoo.models.products.Product
        """
        return self._get('products', id, params)

    def update_product(self, id, **data):
        """
        Change product's properties by id

        :param id: Product id
        :type id: int, str
        :param data: Product properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-properties>`__)
        :rtype: pywoo.models.products.Product
        """
        return self._put('products', id, data)

    def delete_product(self, id, force=True):
        """
        Delete product by id

        :param id: Product id
        :type id: int, str
        :param force: Whether to permanently delete product or not
        :type force: bool
        :rtype: pywoo.models.products.Product
        """
        return self._delete('products', id, {'force' : force})

    def create_product_variation(self, product_id, **data):
        """
        Create variation in product

        :param product_id: Product id
        :type product_id: int, str
        :param data: Product variation properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-properties>`__)
        :rtype: pywoo.models.product_variations.ProductVariation
        """
        return self._create(f'products/{product_id}/variations', data)

    def get_product_variations(self, product_id, id='', **params):
        """
        Get all variations or single variation in product

        :param product_id: Product id
        :type product_id: int, str
        :param id: If specified gets a variation by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of variations (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-variations>`__)
        :rtype: list of pywoo.models.product_variations.ProductVariation,
            pywoo.models.product_variations.ProductVariation
        """
        return self._get(f'products/{product_id}/variations', id, params)

    def update_product_variation(self, product_id, id, **data):
        """
        Change variation's properties in product

        :param product_id: Product id
        :type product_id: int, str
        :param id: Variation id
        :type id: int, str
        :param data: Product variation properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-variation-properties>`__)
        :rtype: pywoo.models.product_variations.ProductVariation
        """
        return self._put(f'products/{product_id}/variations', id, data)

    def delete_product_variation(self, product_id, id):
        """
        Delete variation from product

        :param product_id: Product id
        :type product_id: int, str
        :param id: Variation id
        :type id: int, str
        :rtype: pywoo.models.product_variations.ProductVariation
        """
        return self._delete(f'products/{product_id}/variations', id, {'force': True})

    def create_product_attribute(self, **data):
        """
        Create product attribute

        :param data: Product attribute properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-properties>`__)
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return self._create('products/attributes', data)

    def get_product_attributes(self, id='', **params):
        """
        Get all or single product attribute by id

        :param id: If specified gets a product attribute by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of product attributes (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-attributes>`__)
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return self._get('products/attributes', id, params)

    def update_product_attribute(self, id, **data):
        """
        Change product attribute's properties by id

        :param id: Product attribute id
        :type id: int, str
        :param data: Product attribute properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-properties>`__)
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return self._put('products/attributes', id, data)

    def delete_product_attribute(self, id):
        """
        Delete product attribute by id

        :param id: Product attribute id
        :type id: int, str
        :rtype: pywoo.models.product_attributes.ProductAttribute
        """
        return self._delete('products/attributes', id, {'force': True})

    def create_product_attribute_term(self, product_attribute_id, **data):
        """
        Create new product attribute term

        :param product_attribute_id: Product attribute id
        :type product_attribute_id: int, str
        :param data: Product attribute term properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-term-properties>`__)
        :rtype: pywoo.models.product_attribute_terms.ProductAttributeTerm
        """
        return self._create(f'products/attributes/{product_attribute_id}/terms', data)

    def get_product_attribute_terms(self, product_attribute_id, id='', **params):
        """
        Get all or single product attribute term from product attribute

        :param product_attribute_id: Product attribute id
        :type product_attribute_id: int, str
        :param id: If specified gets a product attribute term by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of product attributes terms (`Full
            list of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-attribute-terms>`__)
        :rtype: list of pywoo.models.product_attribute_terms.ProductAttributeTerm,
            pywoo.models.product_attribute_terms.ProductAttributeTerm
        """
        return self._get(f'products/attributes/{product_attribute_id}/terms', id, params)

    def update_product_attribute_term(self, product_attribute_id, id, **data):
        """
        Change product attribute term's properties by id

        :param product_attribute_id: Product attribute id
        :type product_attribute_id: int, str
        :param id: Product attribute term id
        :type id: int, str
        :param data: Product attribute term properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attribute-term-properties>`__)
        :rtype: pywoo.models.product_attribute_terms.ProductAttributeTerm
        """
        return self._put(f'products/attributes/{product_attribute_id}/terms', id, data)

    def delete_product_attribute_term(self, product_attribute_id, id):
        """
        Delete product attribute term from product attribute

        :param product_attribute_id: Product attribute id
        :type product_attribute_id: int, str
        :param id: Product attribute term id
        :type id: int, str
        :rtype: pywoo.models.product_attribute_terms.ProductAttributeTerm
        """
        return self._delete(f'products/attributes/{product_attribute_id}/terms', id, {'force': True})

    def create_product_category(self, **data):
        """
        Create new product category

        :param data: Product category properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-category-properties>`__)
        :rtype: pywoo.models.product_categories.ProductCategory
        """
        return self._create('products/categories', data)

    def get_product_categories(self, id='', **params):
        """
        Get all or a single product category by id

        :param id: If specified gets a product category by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of product category (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-categories>`__)
        :rtype: list of pywoo.models.product_categories.ProductCategory, pywoo.models.product_categories.ProductCategory
        """
        return self._get('products/categories', id, params)

    def update_product_category(self, id, **data):
        """
        Change product category's properties

        :param id: Product category id
        :type id: int, str
        :param data: Product category properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-category-properties>`__)
        :rtype: pywoo.models.product_categories.ProductCategory
        """
        return self._put('products/categories', id, data)

    def delete_product_category(self, id):
        """
        Delete product category by id

        :param id: Product category id
        :type id: int, str
        :rtype: pywoo.models.product_categories.ProductCategory
        """
        return self._delete('products/categories', id, {'force': True})

    def create_product_shipping_class(self, **data):
        """
        Create new product shipping class

        :param data: Product shipping class properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-shipping-class-properties>`__)
        :rtype: pywoo.models.product_shipping_classes.ProductShipping
        """
        return self._create('products/shipping_classes', data)

    def get_product_shipping_classes(self, id='', **params):
        """
        Get all or single product shipping class by id

        :param id: If specified gets a product shipping class by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more product shipping classes (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-shipping-classes>`__)
        :rtype: list of pywoo.models.product_shipping_classes.ProductShipping,
            pywoo.models.product_shipping_classes.ProductShipping
        """
        return self._get('products/shipping_classes', id, params)

    def update_product_shipping_class(self, id, **data):
        """
        Change product shipping class' properties

        :param id: Product shipping class id
        :type id: int, str
        :param data: Product shipping class properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-shipping-class-properties>`__)
        :rtype: pywoo.models.product_shipping_classes.ProductShipping
        """
        return self._put('products/shipping_classes', id, data)

    def delete_product_shipping_class(self, id):
        """
        Delete product shipping class

        :param id: Product shipping class id
        :type id: int,str
        :rtype: pywoo.models.product_shipping_classes.ProductShipping
        """
        return self._delete('products/shipping_classes', id, {'force': True})

    def create_product_tag(self, **data):
        """
        Create new product tag

        :param data: Product tag properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-tag-properties>`__)
        :rtype: pywoo.models.product_tags.ProductTag
        """
        return self._create('products/tags', data)

    def get_product_tags(self, id='', **params):
        """
        Get all or single product tag by id

        :param id: If specified gets a product tag by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more product tags (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-tags>`__)
        :rtype: list of pywoo.models.product_tags.ProductTag, pywoo.models.product_tags.ProductTag
        """
        return self._get('products/tags', id, params)

    def update_product_tag(self, id, **data):
        """
        Change product tag's properties

        :param id: Product tag id
        :type id: int, str
        :param data: Product tag properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-tag-properties>`__)
        :rtype: pywoo.models.product_tags.ProductTag
        """
        return self._put('products/tags', id, data)

    def delete_product_tag(self, id):
        """
        Delete a product tag by id

        :param id: Product tag id
        :type id: int, str
        :rtype: pywoo.models.product_tags.ProductTag
        """
        return self._delete('products/tags', id, {'force': True})

    def create_product_review(self, **data):
        """
        Create new product review

        :param data: Product review properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-review-properties>`__)
        :rtype: pywoo.models.product_reviews.ProductReview
        """
        return self._create('products/reviews', data)

    def get_product_reviews(self, id='', **params):
        """
        Get all or a single product review by id

        :param id: If specified gets a product review by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more product reviews (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-reviews>`__)
        :rtype: list of pywoo.models.product_reviews.ProductReview, pywoo.models.product_reviews.ProductReview
        """
        return self._get('products/reviews', id, params)

    def update_product_review(self, id, **data):
        """
        Change product review's properties

        :param id: Product review id
        :type id: int, str
        :param data: Product review properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-review-properties>`__)
        :rtype: pywoo.models.product_reviews.ProductReview
        """
        return self._put('products/reviews', id, data)

    def delete_product_review(self, id):
        """
        Delete a product review by id

        :param id: Product review id
        :type id: int, str
        :rtype: pywoo.models.product_reviews.ProductReview
        """
        return self._delete('products/reviews', id, {'force': True})

    def create_tax_rate(self, **data):
        """
        Create new tax rate

        :param data: Tax rate properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#tax-rate-properties>`__)
        :rtype: pywoo.models.tax_rates.TaxRate
        """
        return self._create('taxes', data)

    def get_tax_rates(self, id='', **params):
        """
        Get all or a single tax rate by id

        :param id: If specified gets a tax rate by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more tax rates (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-tax-rates>`__)
        :rtype: list of pywoo.models.tax_rates.TaxRate, pywoo.models.tax_rates.TaxRate
        """
        return self._get('taxes', id, params)

    def update_tax_rate(self, id, **data):
        """
        Change tax rate's properties

        :param id: Tax rate id
        :type id: int, str
        :param data: Tax rate properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#tax-rate-properties>`__)
        :rtype: pywoo.models.tax_rates.TaxRate
        """
        return self._put('taxes', id, data)

    def delete_tax_rate(self, id):
        """
        Delete a tax rate by id

        :param id: Tax rate id
        :type id: int, str
        :rtype: pywoo.models.tax_rates.TaxRate
        """
        return self._delete('taxes', id, {'force': True})

    def create_tax_class(self, **data):
        """
        Create new tax class

        :param data: Tax class properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#tax-class-properties>`__)
        :rtype: pywoo.models.tax_classes.TaxClass
        """
        return self._create('taxes/classes', data)

    def get_tax_classes(self):
        """
        Get all tax classes

        :rtype: list of pywoo.models.tax_classes.TaxClass
        """
        return self._get('taxes/classes')

    def delete_tax_class(self, id):
        """
        Delete a tax class by slug

        :param id: Tax class slug
        :type id: str
        :rtype: pywoo.models.tax_classes.TaxClass
        """
        return self._delete('taxes/classes', id, {'force': True})

    def get_payment_gateways(self, id=''):
        """
        Get all or a single payment gateway by id

        :param id: If specified gets a payment gateway by id
        :type id: int, str
        :rtype: list of pywoo.models.payment_gateways.PaymentGateway, pywoo.models.payment_gateways.PaymentGateway
        """
        return self._get('payment_gateways', id)

    def update_payment_gateway(self, id, **data):
        """
        Change payment gateway's properties

        :param id: Payment gateway id
        :type id: int, str
        :param data: Payment gateway properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#payment-gateway-properties>`__)
        :rtype: pywoo.models.payment_gateways.PaymentGateway
        """
        return self._put('payment_gateways', id, data)

    def create_shipping_zone(self, **data):
        """
        Create new shipping zone

        :param data: Shipping zone properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-zone-properties>`__)
        :rtype: pywoo.models.shipping_zones.ShippingZone
        """
        return self._create('shipping/zones', data)

    def get_shipping_zones(self, id=''):
        """
        Get all or single shipping zones by id

        :param id: If specified gets a shipping zone by id
        :type id: int, str
        :rtype: list of pywoo.models.shipping_zones.ShippingZone, pywoo.models.shipping_zones.ShippingZone
        """
        return self._get('shipping/zones', id)

    def update_shipping_zone(self, id, **data):
        """
        Change shipping zone's properties

        :param id: Shipping zone id
        :type id: int, str
        :param data: Shipping zone properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-zone-properties>`__)
        :rtype: pywoo.models.shipping_zones.ShippingZone
        """
        return self._put('shipping/zones', id, data)

    def delete_shipping_zone(self, id):
        """
        Delete a shipping zone by id

        :param id: Shipping zone id
        :type id: int, str
        :rtype: pywoo.models.shipping_zones.ShippingZone
        """
        return self._delete('shipping/zones', id, {'force': True})

    def get_shipping_zone_locations(self, shipping_zone_id):
        """
        Get all shipping zone locations by shipping zone

        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :rtype: list of pywoo.models.shipping_zone_locations.ShippingZoneLocation
        """
        return self._get(f'shipping/zones/{shipping_zone_id}/locations')

    def update_shipping_zone_locations(self, shipping_zone_id, shipping_locations=[]):
        """
        Change shipping zone locations' properties

        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param shipping_locations: List of shipping locations (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-location-properties>`__)
        :type shipping_locations: list of pywoo.models.shipping_zone_locations.ShippingZoneLocation
        :rtype: list of pywoo.models.shipping_zone_locations.ShippingZoneLocation
        """
        return self._put(f'shipping/zones/{shipping_zone_id}/locations', '', shipping_locations)

    def create_shipping_zone_method(self, shipping_zone_id, **data):
        """
        Include shipping zone method in shipping zone

        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param data: Shipping zone method properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-method-properties>`__)
        :rtype: pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return self._create(f'shipping/zones/{shipping_zone_id}/methods', data)

    def get_shipping_zone_methods(self, shipping_zone_id, id=''):
        """
        Get all or single shipping zone method in shipping zone

        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param id: If specified gets a shipping zone method by id
        :type id: int, str
        :rtype: list of pywoo.models.shipping_zone_methods.ShippingZoneMethod,
            pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return self._get(f'shipping/zones/{shipping_zone_id}/methods', id)

    def update_shipping_zone_method(self, shipping_zone_id, id, **data):
        """
        Change shipping zone method's properties

        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param id: Shipping zone method id
        :type id: int, str
        :param data: Shipping zone method properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#shipping-method-properties>`__)
        :rtype: pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return self._put(f'shipping/zones/{shipping_zone_id}/methods', id, data)

    def delete_shipping_zone_method(self, shipping_zone_id, id):
        """
        Delete a shipping zone method by id

        :param shipping_zone_id: Shipping zone id
        :type shipping_zone_id: int, str
        :param id: Shipping zone method id
        :type id: int, str
        :rtype: pywoo.models.shipping_zone_methods.ShippingZoneMethod
        """
        return self._delete(f'shipping/zones/{shipping_zone_id}/methods', id, {'force': True})

    def get_shipping_methods(self, id=''):
        """
        Get all or single shipping method by id

        :param id: If specified gets a shipping method by id
        :type id: int, str
        :rtype: list of pywoo.models.shipping_zones.ShippingZone, pywoo.models.shipping_zones.ShippingZone
        """
        return self._get('shipping_methods', id)
