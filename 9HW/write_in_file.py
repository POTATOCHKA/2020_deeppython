import time
import asyncio
import aiohttp
from aiofile import AIOFile

list_of_data = []


async def write_file(data):
    name = f'photo_{int(time.time() * 1000)}'
    async with AIOFile(name, 'wb') as afp:
        await afp.write(data)
        await afp.fsync()


async def fetch(url, session):
    async with session.get(url, allow_redirects=True) as resp:
        data = await resp.read()
        list_of_data.append(data)


async def main(n):
    url = 'https://loremflickr.com/320/240'
    tasks = []
    tasks_2 = []

    async with aiohttp.ClientSession() as session:
        for i in range(n):
            tasks.append(asyncio.create_task(fetch(url, session)))
        await asyncio.gather(*tasks)
        for i in range(n):
            tasks_2.append(asyncio.create_task(write_file(list_of_data[i])))
        await asyncio.gather(*tasks_2)


if __name__ == '__main__':
    print('how many images tou want?')
    n = int(input())
    t1 = time.time()
    asyncio.run(main(n))
    t2 = time.time()
    print('TT', t2 - t1)
