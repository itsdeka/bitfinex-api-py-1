# python -c "import examples.websocket.derivatives_status"

import os

from bfxapi.client import Client, Constants
from bfxapi.websocket.enums import Error, OrderType, Channels
from bfxapi.websocket.typings import Subscriptions, DerivativesStatus

from bfxapi.websocket import BfxWebsocketClient


bfx = Client(
    WSS_HOST=Constants.WSS_HOST,
    API_KEY=os.getenv("BFX_API_KEY"),
    API_SECRET=os.getenv("BFX_API_SECRET")
)

@bfx.wss.on('derivatives_status_update')
def log_derivatives_status(subscription: Subscriptions.DerivativesStatus, derivatives_status: DerivativesStatus):
    print(subscription)
    print(derivatives_status)

@bfx.wss.on("wss-error")
def on_wss_error(code: Error, msg: str):
    print(code, msg)

@bfx.wss.once("open")
async def open():
    await bfx.wss.subscribe(Channels.STATUS, key="deriv:tBTCF0:USTF0")

bfx.wss.run()