from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import parse_date_time, to_json, ClassParser


@ClassParser(url_class="orders")
class Order(ApiObject):
    ro_attributes = {'id', 'number', 'order_key', 'created_via', 'version', 'date_created', 'date_created_gmt',
                     'date_modified', 'date_modified_gmt', 'discount_total', 'discount_tax', 'shipping_total',
                     'shipping_tax', 'cart_tax', 'total', 'total_tax', 'prices_include_tax', 'customer_ip_address',
                     'customer_user_agent', 'date_paid', 'date_paid_gmt', 'date_completed', 'date_completed_gmt',
                     'cart_hash', 'tax_lines', 'refunds'}
    wo_attributes = {'set_paid'}
    rw_attributes = {'parent_id', 'status', 'currency', 'customer_id', 'customer_note', 'billing', 'shipping',
                     'payment_method', 'payment_method_title', 'transaction_id', 'meta_data', 'line_items',
                     'shipping_lines', 'fee_lines', 'coupon_lines'}

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
    def delete_order(cls, api, id, **params):
        return api.delete_order(id, **params)

    def update(self):
        return self._api.update_order(**to_json(self))

    def delete(self):
        return self._api.delete_order(self.id)
    
    def refresh(self):
        self.__dict__ = self._api.get_orders(id=self.id).__dict__


@ClassParser(url_class="orders")
class OrderBilling(ApiProperty):
    rw_attributes = {'first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state', 'postcode',
                     'country', 'email', 'phone'}


@ClassParser(url_class="orders")
class OrderShipping(ApiProperty):
    rw_attributes = {'first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state', 'postcode',
                     'country'}


@ClassParser(url_class="orders")
class OrderLineItems(ApiProperty):
    ro_attributes = {'id', 'subtotal_tax', 'total', 'total_tax', 'taxes', 'meta_data', 'sku', 'price'}
    rw_attributes = {'name', 'product_id', 'variation_id', 'quantity', 'tax_class', 'subtotal'}


@ClassParser(url_class="orders")
class OrderShippingLine(ApiProperty):
    ro_attributes = {'id', 'total_tax', 'taxes'}
    rw_attributes = {'method_title', 'method_id', 'total', 'meta_data'}


@ClassParser(url_class="orders")
class OrderFeeLine(ApiProperty):
    ro_attributes = {'id', 'total_tax', 'taxes'}
    rw_attributes = {'name', 'tax_class', 'tax_status', 'total', 'meta_data'}


@ClassParser(url_class="orders")
class OrderCouponLine(ApiProperty):
    ro_attributes = {'id', 'discount', 'discount_tax'}
    rw_attributes = {'code', 'meta_data'}


@ClassParser(url_class="orders")
class OrderRefund(ApiProperty):
    ro_attributes = {'id', 'reason', 'total'}


@ClassParser(url_class="orders")
class OrderTax(ApiProperty):
    ro_attributes = {'id', 'rate_code', 'rate_id', 'label', 'compound', 'tax_total', 'shipping_tax_total'}
    rw_attributes = {'meta_data'}
