import requests
import os
from time import time

from utils.oauth import OAuth

class ApiWoo():

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
    
    def get_products(self):
        resp = requests.get(
            self.__get_oauth_url(f'{self.url}/products', 'GET'),
        )
        return resp.json()