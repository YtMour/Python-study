import multiprocessing
import time

def push(li):
    print(id(li))
    while 1:
        print('正在存放数据')
        li.append('yt')
        time.sleep(1)

def pop(li):
    print(id(li))
    while 1:
        if li:
            print('我正在拿数据'+ str(li.pop()))
            time.sleep(1)

def mian():
    #不是共享内存，是代理服务器操作
    li=multiprocessing.Manager().list()
    print(id(li))

    p1=multiprocessing.Process(target=push, args=(li,))
    p2=multiprocessing.Process(target=pop, args=(li,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    mian()