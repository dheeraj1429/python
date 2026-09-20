import aiohttp
import asyncio

async def fetch_data(session, url):
  async with session.get(url) as response:
    print("Status:", response.status)
    print("Content-type:", response.headers['content-type'])

async def main():
  async with aiohttp.ClientSession() as session:
    urls = ["https://httpbin.org/delay/2"] * 2
    task = [fetch_data(session=session, url=i) for i in urls]
    await asyncio.gather(*task)


asyncio.run(main())