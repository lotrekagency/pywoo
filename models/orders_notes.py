from datetime import datetime

from utils.models import ApiObject


class OrderNote(ApiObject):
    def __init__(self, id, author, date_created, date_created_gmt, note, customer_note, added_by_user, api):
        super().__init__(api)
        self._id = id
        self._author = author
        self._date_created = datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%S')
        self._date_created_gmt = datetime.strptime(date_created_gmt, '%Y-%m-%dT%H:%M:%S')
        self.note = note
        self.customer_note = customer_note
        self.added_by_user = added_by_user

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
