from utils.models import ApiObject
from utils.parse import parse_date_time, to_json, ClassParser


@ClassParser()
class ProductReview(ApiObject):
    def __init__(self, id, date_created, date_created_gmt, product_id, status, reviewer, reviewer_email, review, rating,
                 verified, api, url):
        super().__init__(api, url)
        self._id = id
        self._date_created = parse_date_time(date_created)
        self._date_created_gmt = parse_date_time(date_created_gmt)
        self.product_id = product_id
        self.status = status
        self.reviewer = reviewer
        self.reviewer_email = reviewer_email
        self.review = review
        self.rating = rating
        self.verified = verified

    @classmethod
    def get_product_reviews(cls, api, id='', **params):
        return api.get_product_reviews(id, **params)

    @classmethod
    def create_product_review(cls, api, **kwargs):
        return api.create_product_review(**kwargs)

    @classmethod
    def edit_product_review(cls, api, id, **kwargs):
        return api.update_product_review(id, **kwargs)

    @classmethod
    def delete_product_review(cls, api, id):
        return api.delete_product_review(id)

    def update(self):
        return self._api.update_product_review(self.id, **to_json(self))

    def delete(self):
        return self._api.delete_product_review(self.id)

    @property
    def id(self):
        return self._id

    @property
    def date_created(self):
        return self._date_created

    @property
    def date_created_gmt(self):
        return self._date_created_gmt
