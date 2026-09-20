import asyncio
import time

# async def do_something():
#   print("Starting doing something...")
#   await asyncio.sleep(3)
#   print("Ending doing something....")

# asyncio.run(do_something())

async def do_something(name: str) -> str:
  print(f"Starting doing something... for #{name}")
  await asyncio.sleep(3)
  # time.sleep(3)
  print(f"Ending doing something.... for #{name}")
  return f"done_{name}"

async def do_something2(name: str) -> str:
  print(f"Starting doing something 2... for #{name}")
  await asyncio.sleep(1)
  # time.sleep(2)
  print(f"Ending doing something 2.... for #{name}")
  return f"done_{name}"

async def main():
  print("Started main function...")
  # response1 = await asyncio.gather(do_something(name="01"))
  # response2 = await asyncio.gather(do_something2(name="02"))
  # print(response1, response2)
  response = await asyncio.gather(
    do_something(name="01"),
    do_something2(name="02"),
  )
  print(response)
  print("Ended main function...")

asyncio.run(main())