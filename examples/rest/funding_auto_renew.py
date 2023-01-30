# python -c "import examples.rest.funding_auto_renew"

import os

from bfxapi.client import Client, Constants

bfx = Client(
    REST_HOST=Constants.REST_HOST,
    API_KEY=os.getenv("BFX_API_KEY"),
    API_SECRET=os.getenv("BFX_API_SECRET")
)

notification = bfx.rest.auth.submit_funding_toggle_auto_renew(
    status=1,
    currency="USD",
    amount="150",
    rate="0",  # FRR
    period=2
)

print("Renew toggle notification:", notification)