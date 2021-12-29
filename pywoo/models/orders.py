from pywoo.utils.models import ApiObject, ApiProperty
from pywoo.utils.parse import to_dict, ClassParser


@ClassParser(url_class="orders")
class Order(ApiObject):
    """
    Class for handling order objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-properties>`__
    """
    _ro_attributes = {
        'id', 'number', 'order_key', 'created_via', 'version', 'date_created',
        'date_modified', 'discount_total', 'discount_tax', 'shipping_total',
        'shipping_tax', 'cart_tax', 'total', 'total_tax', 'prices_include_tax', 'customer_ip_address',
        'customer_user_agent', 'date_paid', 'date_completed',
        'cart_hash', 'tax_lines', 'refunds'
    }
    _wo_attributes = {'set_paid'}
    _rw_attributes = {
        'parent_id', 'status', 'currency', 'customer_id', 'customer_note', 'billing', 'shipping',
        'payment_method', 'payment_method_title', 'transaction_id', 'line_items',
        'shipping_lines', 'fee_lines', 'coupon_lines'
    }

    @classmethod
    def get_orders(cls, api, id='', **params):
        """
        Get all orders or a single order by id

        :param api: API object
        :type api: pywoo.Api
        :param id: If specified gets a single order by id
        :type id: int, str
        :param params: Parameters that can be used when retrieving order(s);
            list of parameters:
             - `Single order <https://woocommerce.github.io/woocommerce-rest-api-docs/#retrieve-an-order>`_
             - `List of orders <https://woocommerce.github.io/woocommerce-rest-api-docs/#list-all-orders>`_
        :rtype: list of pywoo.models.orders.Order, pywoo.models.orders.Order
        """
        return api.get_orders(id, **params)

    @classmethod
    def create_order(cls, api, **data):
        """
        Create new order

        :param api: API object
        :type api: pywoo.Api
        :param data: Properties for creating a new order (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-properties>`__)
        :rtype: pywoo.models.orders.Order
        """
        return api.create_order(**data)

    @classmethod
    def edit_order(cls, api, id, **data):
        """
        Update order properties by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Order id
        :type id: int, str
        :param data: Properties to update (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-properties>`__)
        :rtype: pywoo.models.orders.Order
        """
        return api.update_order(id, **data)

    @classmethod
    def delete_order(cls, api, id, force=True):
        """
        Delete order by id

        :param api: API object
        :type api: pywoo.Api
        :param id: Order id
        :type id: int, str
        :param force: Whether to permanently delete order or not
        :type force: bool
        :rtype: pywoo.models.orders.Order
        """
        return api.delete_order(id, force)

    def update(self):
        """
        Push order properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.orders.Order.refresh()` method or use the returned object which is updated.

        :return: Order with updated properties coming from the REST API
        :rtype: pywoo.models.orders.Order
        """
        return self._api.update_order(**to_dict(self))

    def delete(self, force=True):
        """
        Delete order. The object can't be used anymore after its deletion.

        :param force: Whether to permanently delete order or not
        :type force: bool
        :return: Deleted coupon code
        :rtype: pywoo.models.coupon.Coupon
        """
        return self._api.delete_order(self.id, force)

    def refresh(self):
        """
        Refresh order properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_orders(id=self.id).__dict__


@ClassParser(url_class="orders")
class OrderBilling(ApiProperty):
    """
    Class for handling order billing properties inside :class:`~pywoo.models.orders.Order` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-billing-properties>`__
    """
    _rw_attributes = {
        'first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state', 'postcode',
        'country', 'email', 'phone'
    }


@ClassParser(url_class="orders")
class OrderShipping(ApiProperty):
    """
    Class for handling order shipping properties inside :class:`~pywoo.models.orders.Order` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-shipping-properties>`__
    """
    _rw_attributes = {
        'first_name', 'last_name', 'company', 'address_1', 'address_2', 'city', 'state', 'postcode',
        'country'
    }


@ClassParser(url_class="orders")
class OrderLineItems(ApiProperty):
    """
    Class for handling order line item properties inside :class:`~pywoo.models.orders.Order` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-line-items-properties>`__
    """
    _ro_attributes = {'id', 'subtotal_tax', 'total', 'total_tax', 'taxes', 'meta_data', 'sku', 'price'}
    _rw_attributes = {'name', 'product_id', 'variation_id', 'quantity', 'tax_class', 'subtotal'}


@ClassParser(url_class="orders")
class OrderShippingLine(ApiProperty):
    """
    Class for handling order shipping lines properties inside :class:`~pywoo.models.orders.Order` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-shipping-line-properties>`__
    """
    _ro_attributes = {'id', 'total_tax', 'taxes'}
    _rw_attributes = {'method_title', 'method_id', 'total', 'meta_data'}


@ClassParser(url_class="orders")
class OrderFeeLine(ApiProperty):
    """
    Class for handling order fee line properties inside :class:`~pywoo.models.orders.Order` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-fee-line-properties>`__
    """
    _ro_attributes = {'id', 'total_tax', 'taxes'}
    _rw_attributes = {'name', 'tax_class', 'tax_status', 'total', 'meta_data'}


@ClassParser(url_class="orders")
class OrderCouponLine(ApiProperty):
    """
    Class for handling order coupon line properties inside :class:`~pywoo.models.orders.Order` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-coupon-line-properties>`__
    """
    _ro_attributes = {'id', 'discount', 'discount_tax'}
    _rw_attributes = {'code', 'meta_data'}


@ClassParser(url_class="orders")
class OrderRefund(ApiProperty):
    """
    Class for handling order refund properties inside :class:`~pywoo.models.orders.Order` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-refund-properties>`__
    """
    _ro_attributes = {'id', 'reason', 'total'}


@ClassParser(url_class="orders")
class OrderTax(ApiProperty):
    """
    Class for handling order tax properties inside :class:`~pywoo.models.orders.Order` objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-tax-properties>`__
    """
    _ro_attributes = {'id', 'rate_code', 'rate_id', 'label', 'compound', 'tax_total', 'shipping_tax_total'}
    _rw_attributes = {'meta_data'}
