

#操作原子性   最小的不可切分的过程
#num = num + 1 两部分 加法 赋值
#牺牲时间  增加安全

import  threading

LOCK=threading.Lock()
num=0

def add():
    global num
    for i in range(1000000):
        LOCK.acquire()
        num+= 1
        LOCK.release()

def sub():
    global num
    for i in range(1000000):
        LOCK.acquire()
        num-= 1
        LOCK.release()

t1 = threading.Thread(target=add)
t2 = threading.Thread(target=sub)

t1.start()
t2.start()


t1.join()
t2.join()

print('num:',num)