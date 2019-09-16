from datetime import datetime
from utils.models import ApiObject
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


class RefundLine:
    def __init__(self, id=None, name=None, product_id=None, variation_id=None, quantity=None, tax_class=None,
                 subtotal=None, subtotal_tax=None, total=None, total_tax=None, taxes=[], meta_data=[], sku=None,
                 price=None):
        self._id = id
        self.name = name
        self.product_id = product_id
        self.variation_id = variation_id
        self.quantity = quantity
        self.tax_class = tax_class
        self.subtotal = subtotal
        self._subtotal_tax = subtotal_tax
        self.total = total
        self._total_tax = total_tax
        self.taxes = taxes
        self.meta_data = meta_data
        self._sku = sku
        self._price = price

    @property
    def id(self):
        return self._id

    @property
    def subtotal_tax(self):
        return self._subtotal_tax

    @property
    def total_tax(self):
        return self._total_tax

    @property
    def sku(self):
        return self._sku

    @property
    def price(self):
        return self._price


class RefundItemLine:
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
