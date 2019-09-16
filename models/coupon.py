from utils.models import ApiObject
from utils.parse import from_json, parse_date_time


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
        self.product_ids = product_ids # TODO put a list of product objects
        self.excluded_product_ids = excluded_product_ids # TODO same as above
        self.usage_limit = usage_limit
        self.usage_limit_per_user = usage_limit_per_user
        self.limit_usage_to_x_items = limit_usage_to_x_items
        self.free_shipping = free_shipping
        self.product_categories = product_categories # TODO put a list of objects
        self.excluded_product_categories = excluded_product_categories # TODO same as above
        self.exclude_sale_items = exclude_sale_items
        self.minimum_amount = minimum_amount
        self.maximum_amount = maximum_amount
        self.email_restrictions = email_restrictions
        self._used_by = used_by # TODO same as others
        self.meta_data = meta_data

    @classmethod
    def get_coupon(cls, api, id):
        return from_json(api.get_coupons(id=id), api)

    @classmethod
    def create_coupon(cls, api, code):
        return from_json(api.create_coupon(code), api)
    
    @classmethod
    def get_coupons(cls, api):
        return from_json(api.get_coupons(), api)

    '''
    @classmethod
    def update_coupon(cls, api, coupon):
    '''

    '''    
    @staticmethod
    def from_json(json_data, api):
        if(json_data is list):
            coupons = []
            for index, json_element in enumerate(json_data):
                coupons[index] = Coupon.from_json(json_element, api)
            return coupons
        return Coupon(json_data['id'], json_data['code'], json_data['amount'], json_data['date_created'], json_data['date_created_gmt'], json_data['date_modified'], json_data['date_modified_gmt'], json_data['discount_type'], json_data['description'], json_data['date_expires'], json_data['date_expires_gmt'], json_data['usage_count'], json_data['individual_use'], json_data['product_ids'], json_data['excluded_product_ids'], json_data['usage_limit'], json_data['usage_limit_per_user'], json_data['limit_usage_to_x_items'], json_data['free_shipping'], json_data['product_categories'], json_data['excluded_product_categories'], json_data['exclude_sale_items'], json_data['minimum_amount'], json_data['maximum_amount'], json_data['email_restrictions'], json_data['used_by'], json_data['meta_data'], api)
    '''

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
