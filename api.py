import inspect
import sys
from pprint import pprint

import requests
import os
from time import time
from models import *

from utils.oauth import OAuth

mapping = {}


def map_models():
    modules = [key for key, value in sys.modules.items() if key.startswith("models.")]
    for module in modules:
        classes = inspect.getmembers(sys.modules[module], inspect.isclass)
        for _class in classes:
            for member in inspect.getmembers(_class[1]):
                if '__init__' in member:
                    _vars = [arg for arg in inspect.signature(member[1]).parameters.keys() if
                             arg != 'self' and arg != 'api']
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

    def _create(self, url, kwargs):
        resp = requests.post(
            self.__get_oauth_url(f'{self.url}/{url}', 'POST'),
            data=kwargs,
            headers=self._get_default_headers()
        )
        return resp

    def _get(self, url, id=''):
        resp = requests.get(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'GET')
        )
        return resp

    def create_coupon(self, **kwargs):
        return self._create('coupons', kwargs).text

    def get_coupons(self, id=''):
        return self._get('coupons', id=id).text

    def create_customer(self, **kwargs):
        return self._create('customer', kwargs).text

    def get_customers(self, id=''):
        return self._get('customer', id=id).text

