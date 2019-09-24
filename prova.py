import os

from pywoo.pywoo import Api
import pywoo.models

api = Api(os.environ["SITE_URL"], os.environ["WOO_CONSUMER_KEY"], os.environ["WOO_CONSUMER_SECRET"])
print(api.get_coupons())

#print(api.get_coupons(id=""))
#print(api.get_product_categories())


