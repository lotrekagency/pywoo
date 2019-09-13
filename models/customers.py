from datetime import datetime
import json

from utils.models import ApiObject, MetaData


class Customer(ApiObject):
    def __init__(self, id, date_created, date_created_gmt, date_modified, date_modified_gmt, email, first_name,
                 last_name, role, username, billing, shipping, is_paying_customer, avatar_url, meta_data, api):
        super().__init__(api)
        self._id = id
        self._date_created = datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%S.%fZ')
        self._date_created_gmt = datetime.strptime(date_created_gmt, '%Y-%m-%dT%H:%M:%S.%fZ')
        self._date_modified = datetime.strptime(date_modified, '%Y-%m-%dT%H:%M:%S.%fZ')
        self._date_modified_gmt = datetime.strptime(date_modified_gmt, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self._role = role
        self.username = username
        # self.password = None # TODO write-only field
        self.billing = billing
        self.shipping = shipping
        self._is_paying_customer = is_paying_customer
        self._avatar_url = avatar_url
        self.meta_data = meta_data

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
    def role(self):
        return self._role

    @property
    def is_paying_customer(self):
        return self._is_paying_customer

    @property
    def avatar_url(self):
        return self._avatar_url


class CustomerBilling:
    def __init__(self, first_name=None, last_name=None, company=None, address_1=None, address_2=None, city=None,
                 state=None, postcode=None, country=None, email=None, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country
        self.email = email
        self.phone = phone


class CustomerShipping:
    def __init__(self, first_name=None, last_name=None, company=None, address_1=None, address_2=None, city=None,
                 state=None, postcode=None, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.postcode = postcode
        self.country = country