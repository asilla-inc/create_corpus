import asyncio
import requests

url = 'https://www.〇〇〇.com'

def ex(i):
    r = requests.get(url)
    return len(r.content)

async def handler(loop):
    async def async_ex(i):
        async with asyncio.Semaphore(20):
            return await loop.run_in_executor(None, ex, i)
    tasks = [async_ex(i) for i in range(100)]
    return await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
data = loop.run_until_complete(handler(loop))