import aiohttp
import asyncio
import time
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.baidu.com') as r:
            print(r.status)
            print(await r.text())
t = time.time()
main()
print(time.time()-t)