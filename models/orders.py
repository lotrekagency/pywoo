from utils.models import ApiObject, ApiProperty
from utils.parse import parse_date_time, to_json


class Order(ApiObject):
    def __init__(self, id, parent_id, number, order_key, created_via, version, status, currency, date_created,
                 date_created_gmt, date_modified, date_modified_gmt, discount_total, discount_tax, shipping_total,
                 shipping_tax, cart_tax, total, total_tax, prices_include_tax, customer_id, customer_ip_address,
                 customer_user_agent, customer_note, billing, shipping, payment_method, payment_method_title,
                 transaction_id, date_paid, date_paid_gmt, date_completed, date_completed_gmt, cart_hash,
                 meta_data, line_items, tax_lines, shipping_lines, fee_lines, coupon_lines, refunds, api, url):
        super().__init__(api, url)
        self._id = id
        self.parent_id = parent_id
        self._number = number
        self._order_key = order_key
        self._created_via = created_via
        self._version = version
        self.status = status
        self.currency = currency
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self._date_modified = parse_date_time(date_modified)
        self._date_modified_gmt = parse_date_time(date_modified_gmt)
        self._discount_total = discount_total
        self._discount_tax = discount_tax
        self._shipping_total = shipping_total
        self._shipping_tax = shipping_tax
        self._cart_tax = cart_tax
        self._total = total
        self._total_tax = total_tax
        self._prices_include_tax = prices_include_tax
        self.customer_id = customer_id
        self._customer_ip_address = customer_ip_address
        self._customer_user_agent = customer_user_agent
        self.customer_note = customer_note
        self.billing = billing
        self.shipping = shipping
        self.payment_method = payment_method
        self.payment_method_title = payment_method_title
        self.transaction_id = transaction_id
        self._date_paid = parse_date_time(date_paid)
        self._date_paid_gmt = parse_date_time(date_paid_gmt)
        self._date_completed = parse_date_time(date_completed)
        self._date_completed_gmt = parse_date_time(date_completed_gmt)
        self._cart_hash = cart_hash
        self.meta_data = meta_data
        self.line_items = line_items
        self._tax_lines = tax_lines
        self.shipping_lines = shipping_lines
        self.fee_lines = fee_lines
        self.coupon_lines = coupon_lines
        self._refunds = refunds
        # self.__set_paid = set_paid # TODO write-only field

    @classmethod
    def get_orders(cls, api, id='', **params):
        return api.get_orders(id, **params)

    @classmethod
    def create_order(cls, api, **kwargs):
        return api.create_order(**kwargs)

    @classmethod
    def edit_order(cls, api, id, **kwargs):
        return api.update_order(id, **kwargs)

    @classmethod
    def delete_order(cls, api, id):
        return api.delete_order(id)

    def update(self):
        return self._api.update_order(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_order(self.id)

    @property
    def id(self):
        return self._id

    @property
    def number(self):
        return self._number

    @property
    def order_key(self):
        return self._order_key

    @property
    def created_via(self):
        return self._created_via

    @property
    def version(self):
        return self._version

    @property
    def date_created(self):
        return self._date_created

    @property
    def date_created_gmt(self):
        return self._date_created_gmt

    @property
    def date_modified(self):
        return self._date_modified

    @property
    def date_modified_gmt(self):
        return self._date_modified_gmt

    @property
    def discount_total(self):
        return self._discount_total

    @property
    def discount_tax(self):
        return self._discount_tax

    @property
    def shipping_total(self):
        return self._shipping_total

    @property
    def shipping_tax(self):
        return self._shipping_tax

    @property
    def cart_tax(self):
        return self._cart_tax

    @property
    def total(self):
        return self._total

    @property
    def total_tax(self):
        return self._total_tax

    @property
    def prices_include_tax(self):
        return self._prices_include_tax

    @property
    def customer_ip_address(self):
        return self._customer_ip_address

    @property
    def customer_user_agent(self):
        return self._customer_user_agent

    @property
    def date_paid(self):
        return self._date_paid

    @property
    def date_paid_gmt(self):
        return self._date_paid_gmt

    @property
    def date_completed(self):
        return self._date_completed

    @property
    def date_completed_gmt(self):
        return self._date_completed_gmt

    @property
    def cart_hash(self):
        return self._cart_hash

    @property
    def tax_lines(self):
        return self._tax_lines

    @property
    def refunds(self):
        return self._refunds


class OrderLineItems(ApiProperty):
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
        self._taxes = taxes
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
    def taxes(self):
        return self._taxes

    @property
    def sku(self):
        return self._sku

    @property
    def price(self):
        return self._price


class OrderShippingLine(ApiProperty):
    def __init__(self, id=None, method_title=None, method_id=None, total=None, total_tax=None, taxes=None,
                 meta_data=[]):
        self._id = id
        self.method_title = method_title
        self.method_id = method_id
        self.total = total
        self._total_tax = total_tax
        self._taxes = taxes
        self.meta_data = meta_data

    @property
    def id(self):
        return self._id

    @property
    def total_tax(self):
        return self._total_tax

    @property
    def taxes(self):
        return self._taxes


class OrderFeeLine(ApiProperty):
    def __init__(self, id=None, name=None, tax_class=None, tax_status=None, total=None, total_tax=None, taxes=[],
                 meta_data=[]):
        self._id = id
        self.name = name
        self.tax_class = tax_class
        self.tax_status = tax_status
        self.total = total
        self._total_tax = total_tax
        self._taxes = taxes
        self.meta_data = meta_data

    @property
    def id(self):
        return self._id

    @property
    def total_tax(self):
        return self._total_tax

    @property
    def taxes(self):
        return self._taxes


class OrderCouponLine(ApiProperty):
    def __init__(self, id=None, code=None, discount=None, discount_tax=None, meta_data=[]):
        self._id = id
        self.code = code
        self._discount = discount
        self._discount_tax = discount_tax
        self.meta_data = meta_data

    @property
    def id(self):
        return self._id

    @property
    def discount(self):
        return self._discount

    @property
    def discount_tax(self):
        return self._discount_tax


class OrderRefund(ApiProperty):
    def __init__(self, id=None, reason=None, total=None):
        self._id = id
        self._reason = reason
        self._total = total

    @property
    def id(self):
        return self._id

    @property
    def reason(self):
        return self._reason

    @property
    def total(self):
        return self._total


class OrderTax(ApiProperty):
    def __init__(self, id=None, rate_code=None, rate_id=None, label=None, compound=None, tax_total=None,
                 shipping_tax_total=None, meta_data=[]):
        self._id = id
        self._rate_code = rate_code
        self._rate_id = rate_id
        self._label = label
        self._compound = compound
        self._tax_total = tax_total
        self._shipping_tax_total = shipping_tax_total
        self.meta_data = meta_data

    @property
    def id(self):
        return self._id

    @property
    def rate_code(self):
        return self._rate_code

    @property
    def rate_id(self):
        return self._rate_id

    @property
    def label(self):
        return self._label

    @property
    def compound(self):
        return self._compound

    @property
    def tax_total(self):
        return self._tax_total

    @property
    def shipping_tax_total(self):
        return self._shipping_tax_total
