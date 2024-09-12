import asyncio

import requests,httpx,aiohttp
import time
"""
request 只有同步  Session 复用socket
requests_test共花费时间： 17.309118270874023
requests_test session共花费时间： 6.3782734870910645

httpx 有同步 也有异步(python)
httpx_test 共花费时间： 24.67528200149536
httpx_test session共花费时间： 5.766239166259766
httpx 异步共花费时间： 0.7269949913024902(100)
httpx 异步共花费时间： 3.6899912357330322(1000)

aiohttp 只有异步(C)
aiohttp_test 异步共花费时间： 0.9277827739715576(100)
aiohttp_test 异步共花费时间： 2.563102960586548(1000)

同步  requests>httpx    session   httpx>requests
异步  httpx>aiohttp     请求多   aiohttp>httpx
"""


headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
}
url='https://docs.aiohttp.org/en/stable/'
# def requests_test():
#     start=time.time()
#     session=requests.Session()
#     session.headers=headers
#
#     for i in range(100):
#         html=session.get(url)
#         print(html.status_code)
#
#     end=time.time()
#     print('requests_test session共花费时间：',end-start)

async def spider(i,client):
    html=await client.get(url)
    print('启动{} {}'.format(i,html.status))

# async def httpx_test():
#     start = time.time()
#     async with httpx.AsyncClient(headers=headers)as client:
#         lists=[]
#         for i in range(1000):
#             lists.append(asyncio.create_task(spider(i,client)))
#         await asyncio.gather(*lists)
#     end=time.time()
#     print('httpx 异步共花费时间：',end-start)

async def aiohttp_test():
    start = time.time()
    async with aiohttp.ClientSession(headers=headers)as client:
        lists=[]
        for i in range(1000):
            lists.append(asyncio.create_task(spider(i,client)))
        await asyncio.gather(*lists)
    end=time.time()
    print('aiohttp_test 异步共花费时间：',end-start)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(aiohttp_test())