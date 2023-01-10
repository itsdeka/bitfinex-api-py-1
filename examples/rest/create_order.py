# python -c "from examples.rest.create_order import *"

from typing import cast

from bfxapi.enums import OrderType
from bfxapi.rest.typings import Order
from bfxapi.utils.flags_helper import calculate_order_flags

from examples.rest.authentication import *

# Create a new order
new_orders_notification = bfx.rest.auth.submit_order(symbol="tBTCUST", amount=0.005, price=10000, type=OrderType.EXCHANGE_LIMIT,
                                       flags=calculate_order_flags(hidden=False))

# The response is a list containing the orders submitted
# In this case we have submitted only 1 order, so we can access it as follows

new_order = new_orders_notification.NOTIFY_INFO[0]
print(new_order)

# Update it
updated_order = bfx.rest.auth.update_order(id=new_order.ID, price=10001)
print(updated_order)

# Delete it
deleted_order = bfx.rest.auth.cancel_order(id=new_order.ID)
print(deleted_order)
