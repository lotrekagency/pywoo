from utils.models import ApiObject
from utils.parse import parse_date_time


class ProductReview(ApiObject):
    def __init__(self, id, date_created, date_created_gmt, product_id, status, reviewer, reviewer_email, review, rating,
                 verified, api):
        super().__init__(api)
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

    @property
    def id(self):
        return self._id

    @property
    def date_created(self):
        return self._date_created

    @property
    def date_created_gmt(self):
        return self._date_created_gmt
