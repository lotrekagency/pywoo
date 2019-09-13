import inspect
import sys
from pprint import pprint

import requests
import os
import json
from time import time
from models import *
from models.coupon import Coupon
from utils.oauth import OAuth

mapping = {}


def map_models():
    modules = [key for key, value in sys.modules.items() if key.startswith("models.")]
    for module in modules:
        classes = inspect.getmembers(sys.modules[module], inspect.isclass)
        for _class in classes:
            for member in inspect.getmembers(_class[1]):
                if '__init__' in member:
                    _vars = frozenset([arg for arg in inspect.signature(member[1]).parameters.keys() if arg != 'self' and arg != 'api'])
                    mapping[_vars] = _class[1]


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
        headers["content-type"] = "application/json;charset=utf-8"
        return headers

    def create_coupon(self, code):
        json_coupon = {
            "code" : code
        }
        resp = requests.post(
            self.__get_oauth_url(f'{self.url}/coupons', 'POST'),
            data = json.dumps(json_coupon),
            headers=self._get_default_headers()
        )
        return resp.json()
    
    def delete_coupon(self, id):
        json_coupon = {
            "id" : id
        }
        resp = requests.delete(
            self.__get_oauth_url(f'{self.url}/coupons', 'DELETE'),
            data = json.dumps(json_coupon),
            headers=self._get_default_headers()
        )
        return resp.json()

    '''
    def update_coupon(self, id):
        json_coupon = Coupon.from_json()
        resp = requests.put(
            self.__get_oauth_url(f'{self.url}/coupons/{id}', 'PUT'),
            data = json.dumps(json_coupon),
            headers=self._get_default_headers()
        )
        return resp.json()
    '''

    def get_coupon(self, id):
        resp = requests.get(
            self.__get_oauth_url(f'{self.url}/coupons/{id}', 'GET')
        )
        return resp.json()

    def get_products(self):
        resp = requests.get(
            self.__get_oauth_url(f'{self.url}/products', 'GET'),
        )
        return resp.json()

    def get_coupons(self):
        resp = requests.get(
            self.__get_oauth_url(f'{self.url}/coupons', 'GET'),
        )
        resp_json = resp.json()
        for index, element in enumerate(resp_json):
            print(resp_json[index])
        #return resp.json()
