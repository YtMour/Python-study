import aiohttp
import asyncio

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
proxy='http://127.0.0.1:7897'   #只支持http
async def main():
    async with aiohttp.ClientSession() as client:
        html=await client.get('https://docs.aiohttp.org/en/stable/', headers=headers, proxy=proxy)
        print(await html.text())
        html.close()


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())