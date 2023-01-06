import os
import sys
import asyncio
sys.path.append('../../../')

from bfxapi.client import Client
from bfxapi.utils.flags_helper import calculate_order_flags

API_KEY = os.getenv("BFX_KEY")
API_SECRET = os.getenv("BFX_SECRET")

bfx = Client(
  API_KEY=API_KEY,
  API_SECRET=API_SECRET
)

async def create_funding():
  response = await bfx.rest.auth.submit_funding_offer(type="LIMIT", symbol="fUSD", amount=1000, rate=0.012, period=7, flags=calculate_order_flags(hidden=True))
  print ("Offer: ", response.notify_info)
async def run():
  await create_funding()

t = asyncio.ensure_future(run())
asyncio.get_event_loop().run_until_complete(t)