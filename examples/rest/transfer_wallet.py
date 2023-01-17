# python -c "from examples.rest.transfer_wallet import *"

import os

from bfxapi.client import Client, Constants

bfx = Client(
    REST_HOST=Constants.REST_HOST,
    API_KEY=os.getenv("BFX_API_KEY"),
    API_SECRET=os.getenv("BFX_API_SECRET")
)

def transfer_wallet():
  response = bfx.rest.auth.submit_wallet_transfer(from_wallet="exchange", to_wallet="funding", from_currency="ETH", to_currency="ETH", amount=0.001)
  print ("Transfer: ", response.NOTIFY_INFO)

def get_existing_deposit_address():
  response = bfx.rest.auth.get_wallet_deposit_address(wallet="exchange", method="bitcoin", renew=False)
  print ("Address: ", response.NOTIFY_INFO)

def create_new_deposit_address():
  response = bfx.rest.auth.get_wallet_deposit_address(wallet="exchange", method="bitcoin", renew=True)
  print ("Address: ", response.NOTIFY_INFO)

def withdraw():
  # tetheruse = Tether (ERC20)
  response = bfx.rest.auth.submit_wallet_withdraw(wallet="exchange", method="tetheruse", amount=1, address="0x742d35Cc6634C0532925a3b844Bc454e4438f44e")
  print ("Address: ", response.NOTIFY_INFO)

def create_lighting_network_deposit_address():
  invoice = bfx.rest.auth.get_deposit_invoice(wallet="funding", currency="LNX", amount=0.001)
  print ("Invoice: ", invoice)

def run():
  transfer_wallet()
  get_existing_deposit_address()
  create_new_deposit_address()
  withdraw()
  create_lighting_network_deposit_address()

run()