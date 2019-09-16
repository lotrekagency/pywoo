from pprint import pprint

import requests
import os
import json
from time import time
from models import *
from models.coupon import Coupon
from utils.oauth import OAuth
from utils.parse import map_models

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

    def _create(self, url, kwargs):
        resp = requests.post(
            self.__get_oauth_url(f'{self.url}/{url}', 'POST'),
            data=kwargs,
            headers=self._get_default_headers()
        )
        if(resp.status_code != 200):
            print("\033[1;31;40mERROR " + str(resp.status_code) + " " + str(resp.json()["message"]) + "\033[0;37;40m")
            return
        print("\033[1;32;40mSTATUS 200 Created successfully\033[0;37;40m")
        return from_json(resp.text, self)

    def _get(self, url, id=''):
        resp = requests.get(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'GET')
        )
        if(resp.status_code != 200):
            print("\033[1;31;40mERROR " + str(resp.status_code) + " " + str(resp.json()["message"]) + "\033[0;37;40m")
            return
        print("\033[1;32;40mSTATUS 200 Read successfully\033[0;37;40m")
        return from_json(resp.text, self)

    def _put(self, url, id, kwargs):
        print(kwargs)
        resp = requests.put(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'PUT'),
            data=kwargs,
            headers=self._get_default_headers()
        )
        if(resp.status_code != 200):
            print("\033[1;31;40mERROR " + str(resp.status_code) + " " + str(resp.json()["message"]) + "\033[0;37;40m")
            return
        print("\033[1;32;40mSTATUS 200 Updated successfully\033[0;37;40m")
        return from_json(resp.text, self)
    
    def _delete(self, url, id):
        resp = requests.delete(
            self.__get_oauth_url(f'{self.url}/{url}/{id}', 'DELETE'),
            headers=self._get_default_headers()
        )
        if(resp.status_code != 200):
            print("\033[1;31;40mERROR " + str(resp.status_code) + " " + str(resp.json()["message"]) + "\033[0;37;40m")
            return
        print("\033[1;32;40mSTATUS 200 Deleted successfully\033[0;37;40m")
        return from_json(resp.text, self) 

    def create_coupon(self, **kwargs):
        return self._create('coupons', kwargs)

    def get_coupons(self, id=''):
        return self._get('coupons', id=id)

    def update_coupon(self, id, **kwargs):
        print(kwargs)
        return self._put('coupons', id, kwargs)

    '''
    def edit_coupon(self, id, data):
        return self._put('coupons', id, json.loads(data))
    '''

    def delete_coupon(self, id):
        return self._delete('coupons', id)

    def create_customer(self, **kwargs):
        return self._create('customer', kwargs)

    def get_customers(self, id=''):
        return self._get('customer', id=id)

