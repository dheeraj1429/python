import asyncio
import time
import threading

def background_worker():
  while True:
    time.sleep(1)
    print(f"Logging the system health")

async def fetch_order():
  await asyncio.sleep(3)
  print("Fetched order")

threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_order())