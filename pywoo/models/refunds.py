from re import search
from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="refunds")
class Refund(ApiObject):
    """
    Class for handling refunds objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#refunds>`__
    """
    _ro_attributes = {'id', 'date_created', 'date_created_gmt'}
    _wo_attributes = {'api_refund'}
    _rw_attributes = {'amount', 'reason', 'refunded_by', 'meta_data', 'line_items'}

    @classmethod
    def get_refunds(cls, api, order_id, id='', **params):
        """
        Get all or a single refunds by id

        :param api: API object
        :type api: pywoo.Api
        :param order_id: Order ID
        :type order_id: int, str
        :param id: If specified gets a refund by id
        :type id: int, str
        :param params: Parameters that should be used only when retrieving more refunds (`Full list of
            parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-refunds>`__)
        :rtype: list of pywoo.models.refunds.Refund,
            pywoo.models.refunds.Refund
        """
        return api.get_refunds(order_id, id, **params)

    @classmethod
    def create_refund(cls, api, order_id, **data):
        """
        Creates a new refund

        :param api: API object
        :type api: pywoo.Api
        :param order_id: Order ID
        :type order_id: int, str
        :param id: If specified gets a refund by id
        :type id: int, str
        :param data: Refund properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-refund-properties>`__)
        :rtype: pywoo.models.refunds.Refund
        """
        return api.create_refund(order_id, **data)

    @classmethod
    def edit_refund(cls, api, order_id, id, **data):
        """
        Change refund's properties

        :param api: API object
        :type api: pywoo.Api
        :param order_id: Order ID
        :type order_id: int, str
        :param id: Refund id
        :type id: int, str
        :param data: Refund properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-refund-properties>`__)
        :rtype: pywoo.models.refunds.Refund
        """
        return api.update_refund(order_id, id, **data)

    @classmethod
    def delete_refund(cls, api, order_id, id):
        """
        Delete a refund by id

        :param api: API object
        :type api: pywoo.Api
        :param order_id: Order ID
        :type order_id: int, str
        :param id: Refund id
        :type id: int, str
        :rtype: pywoo.models.refunds.Refund
        """
        return api.delete_refund(order_id, id)

    def update(self):
        """
        Push refund properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.refunds.Refund.refresh()` method or use the returned object
        which is updated.

        :return: Product with updated properties coming from the REST API
        :rtype: pywoo.models.refunds.Refund
        """
        return self._api.update_refund(self.order_id, self.id, **to_dict(self))

    def delete(self):
        """
        Deletes refund. The object can't be used anymore after its deletion.

        :param force: Whether to permanently delete product or not
        :type force: bool
        :return: Deleted refund
        :rtype: pywoo.models.refunds.Refund
        """
        return self._api.delete_refund(self.order_id, self.id)

    def refresh(self):
        """
        Refresh refund properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_refunds(order_id=self.order_id, id=self.id).__dict__

    @property
    def order_id(self):
        return search(r"orders\/(\d+)\/.*", self._url).group(1)


@ClassParser(url_class="refunds")
class RefundLineItems(ApiProperty):
    """
    Class for handling refunds' items inside :class:`~pywoo.models.refunds.Refund` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-refund-line-items-properties>`__
    """
    _ro_attributes = {'id', 'subtotal_tax', 'total', 'total_tax', 'taxes', 'meta_data', 'sku', 'price'}
    _rw_attributes = {'name', 'product_id', 'variation_id', 'quantity', 'tax_class', 'subtotal'}


@ClassParser(url_class="refunds")
class RefundLineItemTax(ApiProperty):
    """
    Class for handling refunds' items taxes inside :class:`~pywoo.models.refunds.Refund` objects

    `List of properties
    <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-refund-line-item-taxes-properties>`__
    """
    _ro_attributes = {'id', 'total', 'subtotal'}
