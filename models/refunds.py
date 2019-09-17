from datetime import datetime
from utils.models import ApiObject, ApiProperty
from utils.parse import parse_date_time


class Refund(ApiObject):
    def __init__(self, id, date_created, date_created_gmt, amount, reason, refunded_by, refunded_payment, meta_data,
                 line_items, api):
        super().__init__(api)
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
