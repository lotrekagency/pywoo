from pprint import pprint

import requests
import os
import json
from time import time
from models import *
from models.coupon import Coupon
from utils.oauth import OAuth
from utils.parse import map_models, to_json, from_json, add_url_field

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
        if(resp.status_code != 201):
            print("\033[1;31;40mERROR " + str(resp.status_code) + " " + str(resp.json()["message"]) + "\033[0;37;40m")
            return
        print("\033[1;32;40mSTATUS 200 Created successfully\033[0;37;40m")
        return from_json(add_url_field(resp.text, url), self)

    def _get(self, url, id='', params={}):
        resp = requests.get(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'GET'),
            params=params
        )
        if resp.status_code != 200:
            print("\033[1;31;40mERROR " + str(resp.status_code) + " " + str(resp.json()["message"]) + "\033[0;37;40m")
            return
        print("\033[1;32;40mSTATUS 200 Read successfully\033[0;37;40m")
        print(add_url_field(resp.text, url))
        return from_json(add_url_field(resp.text, url), self)

    def _put(self, url, id, kwargs):
        resp = requests.put(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'PUT'),
            data=kwargs,
            headers=self._get_default_headers()
        )
        if(resp.status_code != 200):
            print("\033[1;31;40mERROR " + str(resp.status_code) + " " + str(resp.json()["message"]) + "\033[0;37;40m")
            return
        print("\033[1;32;40mSTATUS 200 Updated successfully\033[0;37;40m")
        return from_json(add_url_field(resp.text, url), self)

    def _delete(self, url, id, params={}):
        resp = requests.delete(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'DELETE'),
            headers=self._get_default_headers(),
            params=params
        )
        if resp.status_code != 200:
            print("\033[1;31;40mERROR " + str(resp.status_code) + " " + str(resp.json()["message"]) + "\033[0;37;40m")
            return
        print("\033[1;32;40mSTATUS 200 Deleted successfully\033[0;37;40m")
        return from_json(add_url_field(resp.text, url), self)

    def create_coupon(self, **data):
        return self._create('coupons', data)

    def get_coupons(self, id='', **params):
        return self._get('coupons', id)

    def update_coupon(self, id, **kwargs):
        return self._put('coupons', id, kwargs)

    def delete_coupon(self, id):
        return self._delete('coupons', id)
        

    def create_customer(self, **data):
        return self._create('customers', data)

    def get_customers(self, id=''):
        return self._get('customers', id)

    def update_customer(self, id, **kwargs):
        return self._put('coupons', id, kwargs)

    def delete_customer(self, id):
        return self._delete('coupons', id)


    def create_product(self, **data):
        return self._create('products', **data)

    def get_products(self, id='', **params):
        return self._get('products', id, params)

    def update_product(self, id, **data):
        return self._put('products', id, data)

    def delete_product(self, id, force=False):
        return self._delete('products', id, force)


    def create_product_variation(self, product_id, **data):
        return self._create('products/%d/variations', data)

    def get_product_variations(self, product_id, id='', **params):
        return self._get('products/%d/variations' % product_id, id, params)

    def update_product_variation(self, product_id, id, **data):
        return self._put('products/%d/variations' % product_id, id, data)

    def delete_product_variation(self, product_id, id):
        return self._delete('products/%d/variations' % product_id, id, {'force': True})
    

    def create_product_attribute(self, **data):
        return self._create('products/attributes', data)

    def get_product_attributes(self, id='', **params):
        return self._get('products/attributes', id, params)

    def update_product_attribute(self, id, **data):
        return self._put('products/attributes', id, data)

    def delete_product_attribute(self, id):
        return self._delete('products/attributes', id, {'force': True})

    def create_product_attribute_term(self, product_attribute_id, **data):
        return self._create('products/attributes/%d/terms' % product_attribute_id, data)

    def get_product_attribute_terms(self, product_attribute_id, id='', **params):
        return self._get('products/attributes/%d/terms' % product_attribute_id, id, params)

    def update_product_attribute_term(self, product_attribute_id, id, **data):
        return self._put('products/attributes/%d/terms' % product_attribute_id, id, data)

    def delete_product_attribute_term(self, product_attribute_id, id):
        return self._delete('products/attributes/%d/terms' % product_attribute_id, id, {'force': True})

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
        return self._get('shipping/zones/%d/locations' % shipping_zone_id)

    def update_shipping_zone_locations(self, shipping_zone_id, shipping_locations):
        return self._put('shipping/zones/%d/locations' % shipping_zone_id, '', shipping_locations)

    def create_shipping_zone_method(self, shipping_zone_id, **data):
        return self._create('shipping/zones/%d/methods' % shipping_zone_id, data)

    def get_shipping_zone_methods(self, shipping_zone_id, id=''):
        return self._get('shipping/zones/%d/methods' % shipping_zone_id, id)

    def update_shipping_zone_method(self, shipping_zone_id, shipping_zone_method_instance_id, **data):
        return self._put('shipping/zones/%d/methods', shipping_zone_method_instance_id, data)

    def delete_shipping_zone_method(self, shipping_zone_id, shipping_zone_method_instance_id):
        return self._delete('shipping/zones/%d/methods', shipping_zone_method_instance_id, {'force': True})

    def get_shipping_method(self, id=''):
        return self._get('shipping_methods', id)
