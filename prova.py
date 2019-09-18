from api import Api
from models.coupon import Coupon
from models.products import Product
from models.orders import Order
from models.customers import Customer
from models.product_variations import ProductVariation
from models.orders_notes import OrderNote
from models.refunds import Refund
from utils.parse import to_json
import json
import types
api = Api()
'''
c = Coupon.get_coupons(api, '36')
print(c.code)
c.code = 'irutortioru'
c.amount = '9.42'
c = api.update_coupon(c.id, **to_json(c))
#c = Coupon.edit_coupon(api, id='36', code="fagiolo")
'''
p = Product.create_product(api)
pv = ProductVariation.create_product_variation(api, p.id)
print(pv)


