import os
from bfxapi.client import Client, Constants

API_KEY = os.getenv("BFX_KEY")
API_SECRET = os.getenv("BFX_SECRET")

bfx = Client(
  REST_HOST=Constants.REST_HOST,
  API_KEY=API_KEY,
  API_SECRET=API_SECRET
)