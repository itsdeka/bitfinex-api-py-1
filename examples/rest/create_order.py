# python -c "from examples.rest.create_order import *"

from bfxapi.enums import OrderType
from examples.rest.authentication import *
from bfxapi.utils.flags_helper import calculate_order_flags

# Create a new order
new_order = bfx.rest.auth.submit_order(symbol="tBTCUST", amount=0.015, price=10000, type=OrderType.EXCHANGE_LIMIT, flags=calculate_order_flags(hidden=False))
print(new_order)

# Update it
updated_order = bfx.rest.auth.update_order(id=new_order["NOTIFY_INFO"]["ID"], price=10001)
print(updated_order)

# Delete it
deleted_order = bfx.rest.auth.cancel_order(id=new_order["NOTIFY_INFO"]["ID"])
print(deleted_order)