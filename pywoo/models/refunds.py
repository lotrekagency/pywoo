from re import search
from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import parse_date_time, to_json, ClassParser


@ClassParser(url_class="refunds")
class Refund(ApiObject):
    ro_attributes = {'id', 'date_created', 'date_created_gmt'}
    wo_attributes = {'api_refund'}
    rw_attributes = {'amount', 'reason', 'refunded_by', 'meta_data', 'line_items'}

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
    
    def refresh(self):
        self.__dict__ = self._api.get_refunds(order_id=self.order_id, id=self.id).__dict__

    @property
    def order_id(self):
        return search(r"orders\/(\d+)\/.*", self._url).group(1)


@ClassParser(url_class="refunds")
class RefundLineItems(ApiProperty):
    ro_attributes = {'id', 'subtotal_tax', 'total', 'total_tax', 'taxes', 'meta_data', 'sku', 'price'}
    rw_attributes = {'name', 'product_id', 'variation_id', 'quantity', 'tax_class', 'subtotal'}


@ClassParser(url_class="refunds")
class RefundLineItemTax(ApiProperty):
    ro_attributes = {'id', 'total', 'subtotal'}
