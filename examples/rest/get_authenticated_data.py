# python -c "import examples.rest.get_authenticated_data"

import os
import time

from bfxapi.client import Client, Constants

bfx = Client(
    REST_HOST=Constants.REST_HOST,
    API_KEY=os.getenv("BFX_API_KEY"),
    API_SECRET=os.getenv("BFX_API_SECRET")
)

now = int(round(time.time() * 1000))


def log_user_info():
    user_info = bfx.rest.auth.get_user_info()
    print(user_info)


def log_login_history():
    login_history = bfx.rest.auth.get_login_history()
    print(login_history)


def log_wallets():
    wallets = bfx.rest.auth.get_wallets()
    print("Wallets:")
    [print(w) for w in wallets]


def log_orders():
    orders = bfx.rest.auth.get_orders(symbol='tBTCUSD')
    print("Orders:")
    [print(o) for o in orders]


def log_orders_history():
    orders = bfx.rest.auth.get_orders_history(symbol='tBTCUSD', start=0, end=now)
    print("Orders:")
    [print(o) for o in orders]


def log_positions():
    positions = bfx.rest.auth.get_positions()
    print("Positions:")
    [print(p) for p in positions]


def log_trades():
    trades = bfx.rest.auth.get_trades_history(symbol='tBTCUSD', start=0, end=now)
    print("Trades:")
    [print(t) for t in trades]


def log_order_trades():
    order_id = 82406909127
    trades = bfx.rest.auth.get_order_trades(symbol='tBTCUSD', order_id=order_id)
    print("Trade orders:")
    [print(t) for t in trades]


def log_funding_offers():
    offers = bfx.rest.auth.get_funding_offers(symbol='fUSD')
    print("Offers:")
    [print(o) for o in offers]


def log_funding_offer_history():
    offers = bfx.rest.auth.get_funding_offers_history(symbol='fUSD', start=0, end=now)
    print("Offers history:")
    [print(o) for o in offers]


def log_funding_loans():
    loans = bfx.rest.auth.get_funding_loans(symbol='fUSD')
    print("Funding loans:")
    [print(l) for l in loans]


def log_funding_loans_history():
    loans = bfx.rest.auth.get_funding_loans_history(symbol='fUSD', start=0, end=now)
    print("Funding loan history:")
    [print(l) for l in loans]


def log_funding_credits():
    credits = bfx.rest.auth.get_funding_credits(symbol='fUSD')
    print("Funding credits:")
    [print(c) for c in credits]


def log_funding_credits_history():
    credit = bfx.rest.auth.get_funding_credits_history(symbol='fUSD', start=0, end=now)
    print("Funding credit history:")
    [print(c) for c in credit]

def log_margin_info():
    btcusd_margin_info = bfx.rest.auth.get_symbol_margin_info('tBTCUSD')
    print(f"tBTCUSD margin info {btcusd_margin_info}")

    sym_all_margin_info = bfx.rest.auth.get_all_symbols_margin_info()
    print(f"Sym all margin info {sym_all_margin_info}")

    base_margin_info = bfx.rest.auth.get_base_margin_info()
    print(f"Base margin info {base_margin_info}")

def run():
    log_user_info()
    log_wallets()
    log_orders()
    log_orders_history()
    log_positions()
    log_trades()
    log_order_trades()
    log_funding_offers()
    log_funding_offer_history()
    log_funding_credits()
    log_funding_credits_history()
    log_margin_info()

run()