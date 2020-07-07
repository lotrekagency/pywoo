from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="customers")
class Customer(ApiObject):
    """
    Class for handling customer objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#customer-properties>`__
    """
    _ro_attributes = {'id', 'date_created', 'date_modified', 'avatar_url'}
    _wo_attributes = {'password'}
    _rw_attributes = {'email', 'first_name', 'last_name', 'username', 'billing', 'shipping'}

    @classmethod
    def get_customers(cls, api, id='', **params):
        """
        Get all customers of a single customer by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a single customer by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of customers (`Full list of parameters
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-customers>`__)
        :rtype: list of pywoo.models.customers.Customer, pywoo.models.customers.Customer
        """
        return api.get_customers(id, **params)

    @classmethod
    def create_customer(cls, api, **data):
        """
        Create a new customer

        :param api: API object
        :type api: pywoo.Api
        :param data: Properties for creating a new customer (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#customer-properties>`__)
        :rtype: pywoo.models.customers.Customer
        """
        return api.create_customer(**data)

    @classmethod
    def edit_customer(cls, api, id, **data):
        """
        Update customer's properties by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Customer id
        :type id: int, str
        :param data: Properties to update (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#customer-properties>`__)
        :rtype: pywoo.models.customers.Customer
        """
        return api.update_customer(id, **data)

    @classmethod
    def delete_customer(cls, api, id, **params):
        """
        Delete customer by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Customer id
        :type id: int, str
        :param params: Additional parameters for deletion (`Full list of parameters
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#delete-a-customer>`__)
        :rtype: pywoo.models.customers.Customer
        """
        return api.delete_customer(id, **params)

    def update(self):
        """
        Push customer properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.customers.Customer.refresh()` method or use the returned object which is updated.

        :return: Customer with updated properties coming from the REST API
        :rtype: pywoo.models.customers.Customer
        """
        return self._api.update_customer(**to_dict(self))

    def delete(self, **params):
        """
        Delete customer. The object can't be used anymore after its deletion.

        :param params: Additional parameters for deletion (`Full list of parameters
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#delete-a-customer>`__)
        :return: Deleted customer
        :rtype: pywoo.models.customers.Customer
        """
        return self._api.delete_customer(self.id, **params)

    def refresh(self):
        """
        Refresh customer properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_customers(id=self.id).__dict__


@ClassParser(url_class="customers")
class CustomerBilling(ApiProperty):
    """
    Class for handling customer billing properties inside :class:`~pywoo.models.customers.Customer` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#customer-billing-properties>`__
    """
    _rw_attributes = {'first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state', 'postcode',
                      'country', 'email', 'phone'}


@ClassParser(url_class="customers")
class CustomerShipping(ApiProperty):
    """
    Class for handling customer shipping properties inside :class:`~pywoo.models.customers.Customer` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#customer-shipping-properties>`__
    """
    _rw_attributes = {'first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state', 'postcode',
                      'country'}
