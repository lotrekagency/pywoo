Pywoo
=======

Pywoo is a Python 3 wrapper for WooCommerce’s API.

Installation
^^^^^^^^^^^^

::

   pip3 install pywoo

How to use it
^^^^^^^^^^^^^

.. code:: python

   from pywoo import Api

   api = Api('http://your_path_to_woocommerce_api', 'your_consumer_key', 'your_consumer_secret')

   my_product = api.create_product(name="Pizza")

   my_product.description = "A delicious margherita"
   my_product.update()

The ``Api`` object will help you in creating, retrieving, editing and
deleting any class exposed by the WooCommerce API.

Also, all classes have instance methods for modifing the objects on the
go and static methods for doing the same stuff the ``Api`` object does.