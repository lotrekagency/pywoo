from api import Api
from models.coupon import Coupon

api = Api()
c = Coupon.get_coupon(api, 36)
print(c.id)
