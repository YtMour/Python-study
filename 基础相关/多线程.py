
import threading

def print1(name):
    for i in range(100):
        print(threading.current_thread())

def print2(name):
    for i in range(100):
        print(threading.current_thread())


t1 = threading.Thread(target=print1,args=('yt',))
t2 = threading.Thread(target=print2,args=('123456',))
#手动设定为 守护线程
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()

print('t1:',t1.daemon)
print('t2:',t2.daemon)

#守护线程 线程都是你主线程的附庸   你结束 我结束
#非守护线程  你主线程结束 和我没有关系  我自己执行完后 才结束


print("主线程结束", threading.current_thread(), threading.main_thread())