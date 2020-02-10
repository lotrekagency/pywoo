from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="coupons")
class Coupon(ApiObject):
    ro_attributes = {'id', 'date_created', 'date_modified', 'usage_count',
                     'used_by'}
    rw_attributes = {'code', 'amount', 'discount_type', 'product_ids', 'usage_limit', 'usage_limit_per_user',
                     'limit_usage_to_x_items', 'free_shipping', 'product_categories', 'excluded_product_categories',
                     'exclude_sale_items', 'minimum_amount', 'maximum_amount', 'email_restrictions'}

    @classmethod
    def get_coupons(cls, api, id='', **params):
        return api.get_coupons(id, **params)

    @classmethod
    def create_coupon(cls, api, **kwargs):
        return api.create_coupon(**kwargs)

    @classmethod
    def edit_coupon(cls, api, id, **kwargs):
        return api.update_coupon(id, **kwargs)

    @classmethod
    def delete_coupon(cls, api, id):
        return api.delete_coupon(id)

    def update(self):
        return self._api.update_coupon(**to_dict(self))

    def delete(self):
        return self._api.delete_coupon(self.id)

    def refresh(self):
        self.__dict__ = self._api.get_coupons(id=self.id).__dict__
