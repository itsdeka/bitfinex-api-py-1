# python -c "import examples.websocket.wallet_balance"

import os

from bfxapi.client import Client, Constants
from bfxapi.websocket.enums import Error, OrderType
from bfxapi.websocket.typings import Notification, Order, Wallet

from bfxapi.websocket import BfxWebsocketClient

bfx = Client(
    WSS_HOST=Constants.WSS_HOST,
    API_KEY=os.getenv("BFX_API_KEY"),
    API_SECRET=os.getenv("BFX_API_SECRET")
)

@bfx.wss.on('wallet_snapshot')
def log_snapshot(wallets: List[Wallet]):
    for wallet in wallets:
        print("Balance: {}".format(wallet))


@bfx.wss.on('wallet_update')
def log_update(wallet: Wallet):
    print("Balance updates: {}".format(wallet))


@bfx.wss.on("wss-error")
def on_wss_error(code: Error, msg: str):
    print(code, msg)


bfx.wss.run()