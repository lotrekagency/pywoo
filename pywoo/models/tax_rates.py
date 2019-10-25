from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_classes=["taxes"])
class TaxRate(ApiObject):
    ro_attributes = {'id'}
    rw_attributes = {'country', 'state', 'postcode', 'city', 'rate', 'name', 'priority', 'compound', 'shipping',
                     'order', 'class'}

    @classmethod
    def get_tax_rates(cls, api, id='', **params):
        return api.get_tax_rates(id, **params)

    @classmethod
    def create_tax_rate(cls, api, **kwargs):
        return api.create_tax_rate(**kwargs)

    @classmethod
    def edit_tax_rate(cls, api, id, **kwargs):
        return api.update_tax_rate(id, **kwargs)

    @classmethod
    def delete_tax_rate(cls, api, id):
        return api.delete_tax_rate(id)

    def update(self):
        self.__dict__ = self._api.update_tax_rate(**to_dict(self)).__dict__

    def delete(self):
        return self._api.delete_tax_rate(self.id)

    def refresh(self):
        self.__dict__ = self._api.get_tax_rates(id=self.id).__dict__
