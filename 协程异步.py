import asyncio

import anyio
import time

async def num(name):
    print('{} start'.format(name))
    await asyncio.sleep(2)
    print('{} end'.format(name))

async def main():
    # t1=[num(1),
    #     num(2),
    #     num(3)]
    # await asyncio.gather(*t1)
    t1 = [asyncio.create_task(num(1)),
          asyncio.create_task(num(2)),
          asyncio.create_task(num(3))]
    await asyncio.wait(t1)


if __name__ == '__main__':
    #声明协程对象  并不会直接运行
    #await 运行协程对象   等待 会一直阻塞到任务接管返回
    asyncio.run(main())