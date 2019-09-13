from api import Api
from models.coupon import Coupon

api = Api()
c = Coupon.create_coupon(api, 'abnssa')
print(c.id)