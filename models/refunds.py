from re import search
from utils.models import ApiObject, ApiProperty
from utils.parse import parse_date_time, to_json, ClassParser


@ClassParser()
class Refund(ApiObject):
    def __init__(self, id, date_created, date_created_gmt, amount, reason, refunded_by, refunded_payment, meta_data,
                 line_items, api, url):
        super().__init__(api, url)
        self._id = id
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self.amount = amount
        self.reason = reason
        self.refunded_by = refunded_by
        self._refunded_payment = refunded_payment
        self.meta_data = meta_data
        self.line_items = line_items
        # self.api_refund = api_refund # TODO write-only

    @classmethod
    def get_refunds(cls, api, order_id, id='', **params):
        return api.get_refunds(order_id, id, **params)

    @classmethod
    def create_refund(cls, api, order_id, **kwargs):
        return api.create_refund(order_id, **kwargs)
        
    @classmethod
    def edit_refund(cls, api, order_id, id, **kwargs):
        return api.update_refund(order_id, id, **kwargs)

    @classmethod
    def delete_refund(cls, api, order_id, id):
        return api.delete_refund(order_id, id)

    def update(self):
        return self._api.update_refund(self.order_id, self.id, **to_json(self))

    def delete(self):
        return self._api.delete_refund(self.order_id, self.id)
    
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
    def refunded_payment(self):
        return self._refunded_payment
    
    @property
    def order_id(self):
        return search(r"orders\/(\d+)\/.*", self._url).group(1)


@ClassParser()
class RefundItemLine(ApiProperty):
    def __init__(self, id=None, total=None, subtotal=None):
        self._id = id
        self._total = total
        self._subtotal = subtotal

    @property
    def id(self):
        return self._id

    @property
    def total(self):
        return self._total

    @property
    def subtotal(self):
        return self._subtotal
