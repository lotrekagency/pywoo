import json

from datetime import datetime
from utils.models import ApiObject, MetaData


class Coupon(ApiObject):
    def __init__(self, id, code, amount, date_created, date_created_gmt, date_modified, date_modified_gmt,
                 discount_type, description, date_expires, date_expires_gmt, usage_count, individual_use, product_ids,
                 excluded_product_ids, usage_limit, usage_limit_per_user, limit_usage_to_x_items, free_shipping,
                 product_categories, excluded_product_categories, exclude_sale_items, minimum_amount, maximum_amount,
                 email_restrictions, used_by, meta_data, api):
        super().__init__(api)
        self._id = id
        self.code = code
        self.amount = amount
        self._date_created = datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%S.%fZ')
        self._date_created_gmt = datetime.strptime(date_created_gmt, '%Y-%m-%dT%H:%M:%S.%fZ')
        self._date_modified = datetime.strptime(date_modified, '%Y-%m-%dT%H:%M:%S.%fZ')
        self._date_modified_gmt = datetime.strptime(date_modified_gmt, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.discount_type = discount_type
        self.description = description
        self.date_expires = datetime.strptime(date_expires, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.date_expires_gmt = datetime.strptime(date_expires_gmt, '%Y-%m-%dT%H:%M:%S.%fZ')
        self._usage_count = usage_count
        self.individual_use = individual_use
        self.product_ids = product_ids # TODO put a list of product objects
        self.excluded_product_ids = excluded_product_ids # TODO same as above
        self.usage_limit = usage_limit
        self.usage_limit_per_user = usage_limit_per_user
        self.limit_usage_to_x_items = limit_usage_to_x_items
        self.free_shipping = free_shipping
        self.product_categories = product_categories # TODO put a list of objects
        self.excluded_product_categories = excluded_product_categories # TODO same as above
        self.minimum_amount = minimum_amount
        self.maximum_amount = maximum_amount
        self.email_restrictions = email_restrictions
        self._used_by = used_by # TODO same as others
        self.meta_data = meta_data

    @classmethod
    def get_coupon(cls, api, id):
        return Coupon.from_json(json.dumps(api.get_coupon(id)), api)

    @classmethod
    def create_coupon(cls, api, code):
        return Coupon.from_json(json.dumps(api.create_coupon(code)), api)

    @staticmethod
    def from_json(json_data, api):
        coupon = json.loads(json_data)
        return Coupon(coupon['id'], coupon['code'], coupon['amount'], coupon['date_created'], coupon['date_created_gmt'], coupon['date_modified'], coupon['date_modified_gmt'], coupon['discount_type'], coupon['description'], coupon['date_expires'], coupon['date_expires_gmt'], coupon['usage_count'], coupon['individual_use'], coupon['product_ids'], coupon['excluded_product_ids'], coupon['usage_limit'], coupon['usage_limit_per_user'], coupon['limit_usage_to_x_items'], coupon['free_shipping'], coupon['product_categories'], coupon['excluded_product_categories'], coupon['exclude_sale_items'], coupon['minimum_amount'], coupon['maximum_amount'], coupon['email_restrictions'], coupon['used_by'], coupon['meta_data'], api)

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
