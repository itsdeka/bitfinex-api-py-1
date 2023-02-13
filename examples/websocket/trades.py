# python -c "import examples.websocket.trades"

import os

from bfxapi.client import Client, Constants
from bfxapi.websocket.enums import Error, OrderType, Channels
from bfxapi.websocket.typings import Subscriptions, Notification, Order, Wallet, Candle, TradeExecuted

from bfxapi.websocket import BfxWebsocketClient

bfx = Client(
    WSS_HOST=Constants.WSS_HOST,
    API_KEY=os.getenv("BFX_API_KEY"),
    API_SECRET=os.getenv("BFX_API_SECRET")
)

@bfx.wss.on('candles_update')
def log_candle(subscription: Subscriptions.Candles, candle: Candle):
  print ("New candle: {}".format(candle))


@bfx.wss.on('t_trade_executed')
def log_trade(subscription: Subscriptions.TradingPairTrades, trade: TradeExecuted):
  print ("New trade: {}".format(trade))

@bfx.wss.on("wss-error")
def on_wss_error(code: Error, msg: str):
    print(code, msg)

@bfx.wss.once("open")
async def open():
    await bfx.wss.subscribe(Channels.CANDLES, key="trade:1m:tBTCUSD")
    await bfx.wss.subscribe(Channels.TRADES, symbol="tBTCUSD")

bfx.wss.run()