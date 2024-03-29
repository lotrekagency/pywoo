from pywoo.utils.models import ApiObject
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="coupons")
class Coupon(ApiObject):
    """
    Class for handling coupon code objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#coupon-properties>`__
    """
    _ro_attributes = {'id', 'date_created', 'date_modified', 'usage_count',
                      'used_by'}
    _rw_attributes = {'code', 'amount', 'discount_type', 'product_ids', 'usage_limit', 'usage_limit_per_user',
                      'limit_usage_to_x_items', 'free_shipping', 'product_categories', 'excluded_product_categories',
                      'exclude_sale_items', 'minimum_amount', 'maximum_amount', 'email_restrictions'}

    @classmethod
    def get_coupons(cls, api, id='', **params):
        """
        Get all coupon codes or a single coupon code by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a single coupon code by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving a list of coupon codes (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-coupons>`__)
        :rtype: list of pywoo.models.coupon.Coupon, pywoo.models.coupon.Coupon
        """
        return api.get_coupons(id, **params)

    @classmethod
    def create_coupon(cls, api, **data):
        """
        Create a new coupon

        :param api: API object
        :type api: pywoo.Api
        :param data: Properties for creating a new coupon code (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#coupon-properties>`__)
        :rtype: pywoo.models.coupon.Coupon
        """
        return api.create_coupon(**data)

    @classmethod
    def edit_coupon(cls, api, id, **data):
        """
        Update coupon code properties by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Coupon code id
        :type id: int, str
        :param data: Properties to update (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#coupon-properties>`__)
        :rtype: pywoo.models.coupon.Coupon
        """
        return api.update_coupon(id, **data)

    @classmethod
    def delete_coupon(cls, api, id, force=True):
        """
        Delete coupon code by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Coupon code id
        :type id: int, str
        :param force: Whether to permanently delete coupon or not
        :type force: bool
        :rtype: pywoo.models.coupon.Coupon
        """
        return api.delete_coupon(id, force)

    def update(self):
        """
        Push coupon code properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.coupon.Coupon.refresh()` method or use the returned object which is updated.

        :return: Coupon code with updated properties coming from the REST API
        :rtype: pywoo.models.coupon.Coupon
        """
        return self._api.update_coupon(**to_dict(self))

    def delete(self, force=True):
        """
        Delete coupon code. The object can't be used anymore after its deletion.

        :param force: Whether to permanently delete coupon or not
        :type force: bool
        :return: Deleted coupon code
        :rtype: pywoo.models.coupon.Coupon
        """
        return self._api.delete_coupon(self.id, force)

    def refresh(self):
        """
        Refresh coupon code properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_coupons(id=self.id).__dict__
