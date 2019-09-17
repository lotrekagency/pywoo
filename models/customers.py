from utils.models import ApiObject, ApiProperty
from utils.parse import parse_date_time, to_json

class Customer(ApiObject):
    def __init__(self, id, date_created, date_created_gmt, date_modified, date_modified_gmt, email, first_name,
                 last_name, role, username, billing, shipping, is_paying_customer, avatar_url, meta_data, api, url):
        super().__init__(api, url)
        self._id = id
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self._date_modified = parse_date_time(date_modified)
        self._date_modified_gmt = parse_date_time(date_modified_gmt)
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

    @classmethod
    def get_customers(cls, api, id=''):
        return api.get_customers(id=id)

    @classmethod
    def create_customer(cls, api, **kwargs):
        return api.create_customer(**kwargs)
    
    @classmethod
    def edit_customer(cls, api, id, **kwargs):
        return api.update_customer(id, **kwargs)

    @classmethod
    def delete_customer(cls, api, id):
        return api.delete_customer(id)

    def update(self):
        return self._api.update_customer(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_customer(self.id)

    @property
    def id(self):
        return self._id

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


class CustomerBilling(ApiProperty):
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


class CustomerShipping(ApiProperty):
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
