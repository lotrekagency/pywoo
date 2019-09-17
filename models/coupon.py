from utils.models import ApiObject
from utils.parse import from_json, to_json, parse_date_time


class Coupon(ApiObject):
    def __init__(self, id, code, amount, date_created, date_created_gmt, date_modified, date_modified_gmt,
                 discount_type, description, date_expires, date_expires_gmt, usage_count, individual_use, product_ids,
                 excluded_product_ids, usage_limit, usage_limit_per_user, limit_usage_to_x_items, free_shipping,
                 product_categories, excluded_product_categories, exclude_sale_items, minimum_amount, maximum_amount,
                 email_restrictions, used_by, meta_data, api, url):
        super().__init__(api, url)
        self._id = id
        self.code = code
        self.amount = amount
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self._date_modified = parse_date_time(date_modified)
        self._date_modified_gmt = parse_date_time(date_modified_gmt)
        self.discount_type = discount_type
        self.description = description
        self.date_expires = parse_date_time(date_expires)
        self.date_expires_gmt = parse_date_time(date_expires_gmt)
        self._usage_count = usage_count
        self.individual_use = individual_use
        self.product_ids = product_ids
        self.excluded_product_ids = excluded_product_ids
        self.usage_limit = usage_limit
        self.usage_limit_per_user = usage_limit_per_user
        self.limit_usage_to_x_items = limit_usage_to_x_items
        self.free_shipping = free_shipping
        self.product_categories = product_categories
        self.excluded_product_categories = excluded_product_categories
        self.exclude_sale_items = exclude_sale_items
        self.minimum_amount = minimum_amount
        self.maximum_amount = maximum_amount
        self.email_restrictions = email_restrictions
        self._used_by = used_by
        self.meta_data = meta_data

    @classmethod
    def get_coupons(cls, api, id='', **params):
        return api.get_coupons(id=id, **params)

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
        print("sihs")
        return self._api.update_coupon(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_coupon(self.id)

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
    def date_modified(self):
        return self._date_modified

    @property
    def date_modified_gmt(self):
        return self._date_modified_gmt

    @property
    def usage_count(self):
        return self._usage_count

    @property
    def used_by(self):
        return self._used_by
