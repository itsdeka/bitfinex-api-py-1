# python -c "from examples.rest.create_funding import *"

from examples.rest.authentication import *
from bfxapi.utils.flags_helper import calculate_order_flags

offer_notification = bfx.rest.auth.submit_funding_offer(type="LIMIT", symbol="fETH", amount=0.5, rate=0.012, period=2, flags=calculate_order_flags(hidden=True))
print("Offer notification: ", offer_notification)

all_offers = bfx.rest.auth.get_funding_offers()
print("Offers: ", all_offers)