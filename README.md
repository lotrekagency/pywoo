# Pywoo 🛒
[![PyPi](https://img.shields.io/pypi/v/pywoo)](https://pypi.org/project/pywoo/)
[![codecov](https://codecov.io/gh/lotrekagency/pywoo/branch/master/graph/badge.svg)](https://codecov.io/gh/lotrekagency/pywoo)
[![Build Status](https://travis-ci.org/lotrekagency/pywoo.svg?branch=master)](https://travis-ci.org/lotrekagency/pywoo)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/lotrekagency/pywoo/blob/master/LICENSE)

Pywoo is a Python 3 wrapper for WooCommerce API.

#### Installation
```
pip3 install pywoo
```

#### How to use it
```python
from pywoo import Api

api = Api('http://your_path_to_woocommerce_api', 'your_consumer_key', 'your_consumer_secret')

my_product = api.create_product(name="Pizza 🍕")

my_product.description = "A delicious margherita"
my_product.update()
```

The `Api` object will help you in creating, retrieving, editing and deleting any class exposed by the WooCommerce API.
It transforms the responses of requests into objects in order to let users manage WooCommerce's elements easily.
Also, all classes have instance methods for modifing the objects on the go and static methods for doing the same stuff
the `Api` object does.


#### How to run tests
```
pytest tests/
```
