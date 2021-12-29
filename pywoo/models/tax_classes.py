from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser


@ClassParser(url_class="classes")
class TaxClass(ApiObject):
    """
    Class for handling tax class objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#tax-classes>`__
    """
    _ro_attributes = {'slug'}
    _rw_attributes = {'name'}

    @classmethod
    def get_tax_classes(cls, api):
        """
        Get all tax classes

        :param api: API object
        :type api: pywoo.Api
        :rtype: list of pywoo.models.tax_classes.TaxClass,
            pywoo.models.tax_classes.TaxClass
        """
        return api.get_tax_classes()

    @classmethod
    def create_tax_class(cls, api, **data):
        """
        Create tax class
        
        :param api: API object
        :type api: pywoo.Api
        :param data: Tax classes along with their properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#tax-classes>`__)
        :rtype: pywoo.models.tax_classes.TaxClass
        """
        return api.create_tax_class(**data)

    @classmethod
    def delete_tax_class(cls, api, slug):
        """
        Delete tax class by slug
        
        :param api: API object
        :type api: pywoo.Api
        :param slug: Tax class slug
        :type slug: str
        :rtype: pywoo.models.tax_classes.TaxClass
        """
        return api.delete_tax_class(slug)

    def delete(self):
        """
        Deletes tax class. The object can't be used anymore after its deletion.

        :return: Deleted tax class
        :rtype: pywoo.models.tax_classes.TaxClass
        """
        return self._api.delete_tax_class(self.slug)
