# python -c "import examples.rest.extra_calcs"

from bfxapi.client import Client, Constants

bfx = Client(
    REST_HOST=Constants.REST_HOST
)

t_symbol_response = bfx.rest.public.get_trading_market_average_price(
    symbol="tBTCUSD",
    amount=-100,
    price_limit="20000.5"
)

print(t_symbol_response.PRICE_AVG)

f_symbol_response = bfx.rest.public.get_funding_market_average_price(
    symbol="fUSD",
    amount=100,
    period=2,
    rate_limit="0.00015"
)

print(f_symbol_response.RATE_AVG)

fx_rate = bfx.rest.public.get_fx_rate(ccy1="USD", ccy2="EUR")

print(fx_rate.CURRENT_RATE)