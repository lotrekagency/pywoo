from api import Api
from models.coupon import Coupon
from models.products import Product
from utils.parse import to_json
import json
api = Api()
'''
c = Coupon.get_coupons(api, '36')
print(c.code)
c.code = 'irutortioru'
c.amount = '9.42'
c = api.update_coupon(c.id, **to_json(c))
#c = Coupon.edit_coupon(api, id='36', code="fagiolo")
'''
#pv = api.create_product_variation('65', description="sdsd")
c = api.get_coupons('36')
c = api.get_products('65')
print(type(c))

