# python -c "import examples.websocket.wallet_balance"

import os

from bfxapi.client import Client, Constants
from bfxapi.websocket.enums import Error, OrderType
from bfxapi.websocket.typings import Notification, Order

from bfxapi.websocket import BfxWebsocketClient

bfx = Client(
    WSS_HOST=Constants.WSS_HOST,
    API_KEY=os.getenv("BFX_API_KEY"),
    API_SECRET=os.getenv("BFX_API_SECRET")
)

@bfx.wss.on('wallet_snapshot')
def log_snapshot(wallets):
    for wallet in wallets:
        print("Balance: {}".format(wallet))


@bfx.wss.on('wallet_update')
def log_update(wallet):
    print("Balance updates: {}".format(wallet))


@bfx.wss.on('wss-error')
def log_error(msg):
    print("Error: {}".format(msg))


bfx.wss.run()