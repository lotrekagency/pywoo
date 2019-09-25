from re import search

from pywoo.utils.models import ApiObject
from pywoo.utils.parse import parse_date_time, ClassParser


@ClassParser(url_class="notes")
class OrderNote(ApiObject):
    ro_attributes = {'id', 'author', 'date_created', 'date_created_gmt'}
    rw_attributes = {'note', 'customer_note'}

    @classmethod
    def get_order_notes(cls, api, order_id, id=''):
        return api.get_order_notes(order_id, id)

    @classmethod
    def create_order_note(cls, api, order_id, **kwargs):
        return api.create_order_note(order_id, **kwargs)
    
    @classmethod
    def delete_order_note(cls, api, order_id, id):
        return api.delete_order_note(order_id, id)

    def delete(self):
        return self._api.delete_order_note(self.order_id, self.id)
    
    def refresh(self):
        self.__dict__ = self._api.get_order_notes(order_id=self.order_id, id=self.id).__dict__
    
    @property
    def order_id(self):
        return search(r"orders\/(\d+)\/.*", self._url).group(1)
