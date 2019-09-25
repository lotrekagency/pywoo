import os

from pywoo.pywoo import Api
import pywoo.models

api = Api(os.environ["SITE_URL"], os.environ["WOO_CONSUMER_KEY"], os.environ["WOO_CONSUMER_SECRET"])
coupon = api.get_coupons()[0]
print(coupon.code)
coupon.code = "isdw"
coupon.update()
print(coupon.code)
coupon.code = "primaa"
print(coupon.code)
coupon.refresh()
print(type(coupon))

#print(api.get_coupons(id=""))
#print(api.get_product_categories())


