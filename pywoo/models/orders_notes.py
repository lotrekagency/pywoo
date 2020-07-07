from re import search

from pywoo.utils.models import ApiObject
from pywoo.utils.parse import ClassParser


@ClassParser(url_class="notes")
class OrderNote(ApiObject):
    """
    Class for handling order note objects

    `List of parameters <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-note-properties>`__
    """
    _ro_attributes = {'id', 'date_created'}
    _rw_attributes = {'note', 'customer_note'}

    @classmethod
    def get_order_notes(cls, api, order_id, id=''):
        """
        Get all notes or single note from order

        :param api: API object
        :type api: pywoo.Api
        :param order_id: Order id
        :type order_id: int, str
        :param id: If specified gets a order note by id
        :type id: int, str
        :rtype: list of pywoo.models.order_notes.OrderNote, pywoo.models.order_notes.OrderNote
        """
        return api.get_order_notes(order_id, id)

    @classmethod
    def create_order_note(cls, api, order_id, **data):
        """
        Add new note to order

        :param api: API object
        :type api: pywoo.Api
        :param order_id: Order id
        :type order_id: int, str
        :param data: Order note properties (`Full list of properties
            <https://woocommerce.github.io/woocommerce-rest-api-docs/#order-note-properties>`__)
        :rtype: pywoo.models.order_notes.OrderNote
        """
        return api.create_order_note(order_id, **data)

    @classmethod
    def delete_order_note(cls, api, order_id, id):
        """
        Delete note from order

        :param api: API object
        :type api: pywoo.Api
        :param order_id: Order id
        :type order_id: int, str
        :param id: Order note id
        :type id: int, str
        :rtype: pywoo.models.order_notes.OrderNote
        """
        return api.delete_order_note(order_id, id)

    def delete(self):
        """
        Push order note properties to Woocommerce REST API.

        **Note**: Woocommerce might update properties when pushing data, but these won't be updated
        on the object itself. If you want to have your properties updated you can call the
        :func:`~pywoo.models.orders_notes.OrderNote.refresh()` method or use the returned object which is updated.

        :return: Order note with updated properties coming from the REST API
        :rtype: pywoo.models.orders_notes.OrderNote
        """
        return self._api.delete_order_note(self.order_id, self.id)

    def refresh(self):
        """
        Refresh order note properties from Woocommerce REST API
        """
        self.__dict__ = self._api.get_order_notes(order_id=self.order_id, id=self.id).__dict__

    @property
    def order_id(self):
        """
        :return: Order ID
        :rtype: str
        """
        return search(r"orders\/(\d+)\/.*", self._url).group(1)
