from re import search

from utils.models import ApiObject
from utils.parse import parse_date_time, to_json


class OrderNote(ApiObject):
    def __init__(self, id, author, date_created, date_created_gmt, note, customer_note, api, url):
        super().__init__(api, url)
        self._id = id
        self._author = author
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self.note = note
        self.customer_note = customer_note
        #self.added_by_user = added_by_user

    @classmethod
    def get_order_notes(cls, api, order_id, id=''):
        return api.get_order_notes(order_id, id=id)

    @classmethod
    def create_order_note(cls, api, order_id, **kwargs):
        return api.create_order_note(order_id, **kwargs)
    
    @classmethod
    def delete_order_note(cls, api, order_id, id):
        return api.delete_order_note(order_id, id)

    def delete(self):
        return self._api.delete_order_note(self.order_id, self.id)

    @property
    def id(self):
        return self._id

    @property
    def author(self):
        return self._author

    @property
    def date_created(self):
        return self._date_created

    @property
    def date_created_gmt(self):
        return self._date_created_gmt
    
    @property
    def order_id(self):
        return self._url.split('/')[1]
