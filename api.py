import requests
import os
import json
from time import time

from utils.oauth import OAuth

class Api():

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
        return resp.json()
