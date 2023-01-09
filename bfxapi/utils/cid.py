import time

def generate_unique_cid():
  return int(round(time.time() * 1000))
