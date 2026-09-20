import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def task(item):
  print(f"Checking item: {item}...")
  time.sleep(3)
  return f"Item {item} in stock available"

async def main():
  loop = asyncio.get_running_loop()
  with ThreadPoolExecutor() as pool:
    result = await loop.run_in_executor(pool, task, "phone1")
    print(result)
  with ThreadPoolExecutor() as pool:
      result = await loop.run_in_executor(pool, task, "phone2")
      print(result)

asyncio.run(main())