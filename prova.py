from api import Api
from models.coupon import Coupon

api = Api()
c = Coupon.get_coupons(api, '36')
print(c.code)
c.code = 'oasi'
c.amount = '9.42'
c = c.reload_coupon(api)
print(c.code)
print(c.amount)