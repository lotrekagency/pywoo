from pywoo.pywoo import Api
from pywoo.models import Product
from pywoo.models import ProductVariation

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


