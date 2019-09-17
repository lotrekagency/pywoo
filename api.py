from pprint import pprint

import requests
import os
import json
from time import time
from models import *
from models.coupon import Coupon
from utils.oauth import OAuth
from utils.parse import map_models, to_json

from utils.parse import from_json

map_models()


class Api:

    def _get_env_var(self, var):
        try:
            return os.environ[var]
        except:
            raise Exception(f"{var} environment variable not defined")

    def __init__(self):
        self.url = self._get_env_var('SITE_URL')
        self.consumer_key = self._get_env_var('WOO_CONSUMER_KEY')
        self.consumer_secret = self._get_env_var('WOO_CONSUMER_SECRET')
        self.version = "wc/v3"

    def __get_oauth_url(self, url, method, **kwargs):
        """ Generate oAuth1.0a URL """
        oauth = OAuth(
            url=url,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            method=method,
            oauth_timestamp=kwargs.get("oauth_timestamp", int(time())),
            version='wc/v3'
        )
        return oauth.get_oauth_url()

    def _get_default_headers(self):
        headers = {}
        return headers

    def _create(self, url, data):
        resp = requests.post(
            self.__get_oauth_url(f'{self.url}/{url}', 'POST'),
            json=data,
            headers=self._get_default_headers()
        )
        if resp.status_code != 201:
            raise Exception(f"\033[1;31;40mHTTP ERROR {resp.status_code} {resp.json()['message']}\033[0m")
        print("\033[1;32;40mSTATUS 200 Created successfully\033[0m")
        return from_json(resp.text, self, url)

    def _get(self, url, id='', params={}):
        resp = requests.get(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'GET'),
            params=params
        )
        if resp.status_code != 200:
            raise Exception(f"\033[1;31;40mHTTP ERROR {resp.status_code} {resp.json()['message']}\033[0m")
        print("\033[1;32;40mSTATUS 200 Read successfully\033[0m")
        return from_json(resp.text, self, url)

    def _put(self, url, id, data):
        resp = requests.put(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'PUT'),
            data=data,
            headers=self._get_default_headers()
        )
        if resp.status_code != 200:
            raise Exception(f"\033[1;31;40mHTTP ERROR {resp.status_code} {resp.json()['message']}\033[0m")
        print("\033[1;32;40mSTATUS 200 Updated successfully\033[0m")
        return from_json(resp.text, self)

    def _delete(self, url, id, params={}):
        resp = requests.delete(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'DELETE'),
            headers=self._get_default_headers(),
            params=params
        )
        if resp.status_code != 200:
            raise Exception(f"\033[1;31;40mHTTP ERROR {resp.status_code} {resp.json()['message']}\033[0m")
        print("\033[1;32;40mSTATUS 200 Deleted successfully\033[0m")
        return from_json(resp.text, self, url)

    def create_coupon(self, **data):
        return self._create('coupons', data)

    def get_coupons(self, id='', **params):
        return self._get('coupons', id, params)

    def update_coupon(self, id, **data):
        return self._put('coupons', id, data)

    def delete_coupon(self, id):
        return self._delete('coupons', id, {'force': True})

    def create_customer(self, **data):
        return self._create('customer', data)

    def get_customers(self, id='', **params):
        return self._get('customer', id, params)

    def update_customer(self, id, *data):
        return self._update('customer', id, data)

    def delete_customer(self, id, **params):
        params['force'] = True
        return self._delete('customer', id, params)

    def create_order(self, **data):
        return self._create('orders', data)

    def get_orders(self, id='', **params):
        return self._get('orders', id, params)

    def update_order(self, id, **data):
        return self._put('orders', id, data)

    def delete_order(self, id, **params):
        return self._delete('orders', id, params)

    def create_order_note(self, order_id, **data):
        return self._create(f'orders/{order_id}/notes', data)

    def get_order_notes(self, order_id, id='', **params):
        return self._get(f'orders/{order_id}/notes', id, params)

    def update_order_notes(self, order_id, id, **data):
        return self._put(f'orders/{order_id}/notes', id, data)

    def delete_order_notes(self, order_id, id):
        return self._delete(f'orders/{order_id}/notes', id, {'force': True})

    def create_refund(self, order_id, **data):
        return self._create(f'orders/{order_id}/refunds', data)

    def get_refunds(self, order_id, id='', **params):
        return self._get(f'orders/{order_id}/refunds', id, params)

    def update_refund(self, order_id, id, **data):
        return self._put(f'orders/{order_id}/refunds', id, data)

    def delete_refund(self, order_id, id):
        return self._delete(f'orders/{order_id}/refunds', id, {'force': True})

    def create_product(self, **data):
        return self._create('products', **data)

    def get_products(self, id='', **params):
        return self._get('products', id, params)

    def update_products(self, id, **data):
        return self._put('products', id, data)

    def delete_products(self, id, **params):
        return self._delete('products', id, params)

    def create_product_variation(self, product_id, **data):
        return self._create(f'products/{product_id}/variations', data)

    def get_product_variations(self, product_id, id='', **params):
        return self._get(f'products/{product_id}/variations', id, params)

    def update_product_variation(self, product_id, id, **data):
        return self._put(f'products/{product_id}/variations', id, data)

    def delete_product_variation(self, product_id, id):
        return self._delete(f'products/{product_id}/variations', id, {'force': True})

    def create_product_attribute(self, **data):
        return self._create('products/attributes', data)

    def get_product_attributes(self, id='', **params):
        return self._get('products/attributes', id, params)

    def update_product_attribute(self, id, **data):
        return self._put('products/attributes', id, data)

    def delete_product_attribute(self, id):
        return self._delete('products/attributes', id, {'force': True})

    def create_product_attribute_term(self, product_attribute_id, **data):
        return self._create(f'products/attributes/{product_attribute_id}/terms', data)

    def get_product_attribute_terms(self, product_attribute_id, id='', **params):
        return self._get(f'products/attributes/{product_attribute_id}/terms', id, params)

    def update_product_attribute_term(self, product_attribute_id, id, **data):
        return self._put(f'products/attributes/{product_attribute_id}/terms', id, data)

    def delete_product_attribute_term(self, product_attribute_id, id):
        return self._delete(f'products/attributes/{product_attribute_id}/terms', id, {'force': True})

    def create_product_category(self, **data):
        return self._create('products/categories', data)

    def get_product_categories(self, id='', **params):
        return self._get('products/categories', params)

    def update_product_category(self, id, **data):
        return self._put('products/categories', id, data)

    def delete_product_category(self, id):
        return self._delete('products/categories', id, {'force': True})

    def create_product_shipping_class(self, **data):
        return self._create('products/shipping_classes', data)

    def get_products_shipping_class(self, id='', **params):
        return self._get('products/shipping_classes', id, params)

    def update_product_shipping_class(self, id, **data):
        return self._put('products/shipping_classes', id, data)

    def delete_product_shipping_class(self, id):
        return self._delete('products/shipping_classes', id, {'force': True})

    def create_product_tag(self, **data):
        return self._create('products/tags', data)

    def get_product_tags(self, id='', **params):
        return self._get('products/tags', id, params)

    def update_product_tag(self, id, **data):
        return self._put('products/tags', id, data)

    def delete_product_tag(self, id):
        return self._delete('products/tags', id, {'force': True})

    def create_product_review(self, **data):
        return self._create('products/reviews', data)

    def get_product_reviews(self, id='', **params):
        return self._get('products/reviews', id, params)

    def update_product_review(self, id, **data):
        return self._put('products/reviews', id, data)

    def delete_product_review(self, id):
        return self._delete('product/reviews', id, {'force': True})

    def create_tax_class(self, **data):
        return self._create('taxes/classes', data)

    def get_tax_classes(self):
        return self._get('taxes/classes')

    def delete_tax_class(self, id):
        return self._delete('taxes/classes', id, {'force': True})

    def get_payment_gateway(self, id=''):
        return self._get('payment_gateways', id)

    def update_payment_gateway(self, id, **data):
        return self._put('payment_gateways', id, data)

    def create_shipping_zone(self, **data):
        return self._create('shipping/zones', data)

    def get_shipping_zone(self, id=''):
        return self._get('shipping/zones', id)

    def update_shipping_zone(self, id, **data):
        return self._put('shipping/zones', id, data)

    def delete_shipping_zone(self, id):
        return self._delete('shipping/zones', id, {'force': True})

    def get_shipping_zone_locations(self, shipping_zone_id):
        return self._get(f'shipping/zones/{shipping_zone_id}/locations')

    def update_shipping_zone_locations(self, shipping_zone_id, shipping_locations):
        return self._put(f'shipping/zones/{shipping_zone_id}/locations', '', shipping_locations)

    def create_shipping_zone_method(self, shipping_zone_id, **data):
        return self._create(f'shipping/zones/{shipping_zone_id}/methods', data)

    def get_shipping_zone_methods(self, shipping_zone_id, id=''):
        return self._get(f'shipping/zones/{shipping_zone_id}/methods', id)

    def update_shipping_zone_method(self, shipping_zone_id, shipping_zone_method_instance_id, **data):
        return self._put(f'shipping/zones/{shipping_zone_id}/methods', shipping_zone_method_instance_id, data)

    def delete_shipping_zone_method(self, shipping_zone_id, shipping_zone_method_instance_id):
        return self._delete(f'shipping/zones/{shipping_zone_id}/methods', shipping_zone_method_instance_id, {'force': True})

    def get_shipping_method(self, id=''):
        return self._get('shipping_methods', id)
