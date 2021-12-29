Quickstart
^^^^^^^^^^

First of all install pywoo in your virtualenv:

::

   pip3 install pywoo

Then you can start coding, here's a little example:

.. code:: python

   from pywoo import Api
   api = Api('http://your_path_to_woocommerce_api', 'your_consumer_key', 'your_consumer_secret')
   my_product = api.create_product(name="Pizza 🍕")
   my_product.description = "A delicious margherita"
   my_product.update()

The ``Api`` object will help you in creating, retrieving, editing and
deleting any class exposed by the WooCommerce API. It transforms the
responses of requests into objects in order to let users manage
WooCommerce’s elements easily. Also, all classes have instance methods
for modifing the objects on the go and static methods for doing the same
stuff the ``Api`` object does.