from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_json, ClassParser


@ClassParser(url_class="reviews")
class ProductReview(ApiObject):
    ro_attributes = {'id', 'date_created', 'date_created_gmt'}
    rw_attributes = {'product_id', 'status', 'reviewer', 'reviewer_email', 'review', 'rating', 'verified'}

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
        return self._api.update_product_review(**to_json(self))

    def delete(self):
        return self._api.delete_product_review(self.id)

    def refresh(self):
        self.__dict__ = self._api.get_product_reviews(id=self.id).__dict__

