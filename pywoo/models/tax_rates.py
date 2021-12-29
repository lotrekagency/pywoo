from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="taxes")
class TaxRate(ApiObject):
    """
    Class for handling tax rates objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#tax-rates>`__
    """
    _ro_attributes = {'id'}
    _rw_attributes = {
        'country', 'state', 'postcode', 'city', 'rate', 'name', 'priority', 'compound', 'shipping',
        'order', 'class'
    }

    @classmethod
    def get_tax_rates(cls, api, id='', **params):
        """
        Get all or a single tax rate by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a tax rate by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more tax rates (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-products>`__)
        :rtype: list of pywoo.models.tax_rates.TaxRate,
            pywoo.models.tax_rates.TaxRate
        """
        return api.get_tax_rates(id, **params)

    @classmethod
    def create_tax_rate(cls, api, **data):
        """
        Creates a new tax rate

        :param api: API object
        :type api: pywoo.Api
        :param data: Tax rate properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#tax-rates>`__)
        :rtype: pywoo.models.tax_rates.TaxRate
        """
        return api.create_tax_rate(**data)

    @classmethod
    def edit_tax_rate(cls, api, id, **data):
        """
        Change tax rate's properties

        :param api: API object
        :type api: pywoo.Api
        :param id: Product id
        :type id: int, str
        :param data: Tax rate properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#tax-rates>`__)
        :rtype: pywoo.models.tax_rates.TaxRate
        """
        return api.update_tax_rate(id, **data)

    @classmethod
    def delete_tax_rate(cls, api, id):
        """
        Delete a tax rate by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Tax rate id
        :type id: int, str
        :rtype: pywoo.models.tax_rates.TaxRate
        """
        return api.delete_tax_rate(id)

    def update(self):
        """
        Push tax rate properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.tax_rates.TaxRate.refresh()` method or use the returned object
        which is updated.

        :return: Tax rate with updated properties coming from the REST API
        :rtype: pywoo.models.tax_rates.TaxRate
        """
        return self._api.update_tax_rate(**to_dict(self))

    def delete(self):
        """
        Deletes tax rate. The object can't be used anymore after its deletion.

        :return: Deleted tax rate
        :rtype: pywoo.models.tax_rates.TaxRate
        """
        return self._api.delete_tax_rate(self.id)

    def refresh(self):
        """
        Refresh tax rate properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_tax_rates(id=self.id).__dict__
