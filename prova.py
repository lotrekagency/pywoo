from api import Api
from models.coupon import Coupon
from models.products import Product
from models.product_variations import ProductVariation
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

pv = api.create_product_variation('65', description="sdsd")
print(pv.description)
pv = ProductVariation.edit_product_variation(api, pv.product_id, pv.id, description="ciao")
print(pv.description)
pv.description = "ciao2"
pv = pv.update()
print(pv.description)


