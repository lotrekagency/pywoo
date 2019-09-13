from api import Api
from models.coupon import Coupon

api = Api()
Coupon.get_coupons(api)
