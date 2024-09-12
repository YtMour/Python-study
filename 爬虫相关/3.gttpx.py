import httpx
import asyncio

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
proxies = {
    'http://': 'http://localhost:7897',
    'https://': 'http://localhost:7897'
    }


async def spider(num):
    print('启动',num)
    async with httpx.AsyncClient(http2=True, proxies=proxies)as client:
        html = await client.get('https://www.python-httpx.org/',headers=headers)
        print(html)


async def mian():
    await asyncio.gather(*[spider(1),spider(2),spider(3)])

if __name__ == '__main__':
    asyncio.run(mian())