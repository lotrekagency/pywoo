from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_json, ClassParser


@ClassParser(url_class="customers")
class Customer(ApiObject):
    ro_attributes = {'id', 'date_created', 'date_created_gmt', 'date_modified', 'date_modified_gmt', 'role',
                     'is_paying_customer', 'avatar_url'}
    wo_attributes = {'password'}
    rw_attributes = {'email', 'first_name', 'last_name', 'username', 'billing', 'shipping', 'meta_data'}

    @classmethod
    def get_customers(cls, api, id='', **params):
        return api.get_customers(id, **params)

    @classmethod
    def create_customer(cls, api, **kwargs):
        return api.create_customer(**kwargs)

    @classmethod
    def edit_customer(cls, api, id, **kwargs):
        return api.update_customer(id, **kwargs)

    @classmethod
    def delete_customer(cls, api, id, **params):
        return api.delete_customer(id, **params)

    def update(self):
        return self._api.update_customer(**to_json(self))

    def delete(self, **params):
        return self._api.delete_customer(self.id, **params)
    
    def refresh(self):
        self.__dict__ = self._api.get_customers(id=self.id).__dict__


@ClassParser(url_class="customers")
class CustomerBilling(ApiProperty):
    rw_attributes = {'first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state', 'postcode',
                     'country', 'email', 'phone'}


@ClassParser(url_class="customers")
class CustomerShipping(ApiProperty):
    rw_attributes = {'first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state', 'postcode',
                     'country'}
