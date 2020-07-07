from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="reviews")
class ProductReview(ApiObject):
    """
    Class for handling product review objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-review-properties>`__
    """
    _ro_attributes = {'id', 'date_created', 'date_created_gmt'}
    _rw_attributes = {'product_id', 'status', 'reviewer', 'reviewer_email', 'review', 'rating', 'verified'}

    @classmethod
    def get_product_reviews(cls, api, id='', **params):
        """
        Get all or a single product review by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a product review by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more product reviews (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-product-reviews>`__)
        :rtype: list of pywoo.models.product_reviews.ProductReview, pywoo.models.product_reviews.ProductReview
        """
        return api.get_product_reviews(id, **params)

    @classmethod
    def create_product_review(cls, api, **data):
        """
        Create new product review

        :param api: API object
        :type api: pywoo.Api
        :param data: Product review properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-review-properties>`__)
        :rtype: pywoo.models.product_reviews.ProductReview
        """
        return api.create_product_review(**data)

    @classmethod
    def edit_product_review(cls, api, id, **data):
        """
        Change product review's properties

        :param api: API object
        :type api: pywoo.Api
        :param id: Product review id
        :type id: int, str
        :param data: Product review properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#product-review-properties>`__)
        :rtype: pywoo.models.product_reviews.ProductReview
        """
        return api.update_product_review(id, **data)

    @classmethod
    def delete_product_review(cls, api, id):
        """
        Delete a product review by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Product review id
        :type id: int, str
        :rtype: pywoo.models.product_reviews.ProductReview
        """
        return api.delete_product_review(id)

    def update(self):
        """
        Push product review properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.product_reviews.ProductReview.refresh()` method or use the returned object
        which is updated.

        :return: Product review with updated properties coming from the REST API
        :rtype: pywoo.models.product_reviews.ProductReview
        """
        return self._api.update_product_review(**to_dict(self))

    def delete(self):
        """
        Delete product review. The object can't be used anymore after its deletion.

        :return: Deleted product review
        :rtype: pywoo.models.product_reviews.ProductReview
        """
        return self._api.delete_product_review(self.id)

    def refresh(self):
        """
        Refresh product review properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_product_reviews(id=self.id).__dict__
