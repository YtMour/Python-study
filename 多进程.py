

import multiprocessing
import time

def num(name):
    print('run process {}'.format(name))
    time.sleep(2)
    print('run process {} end'.format(name))

if __name__ == '__main__':
    #进程池   在一开始就创建好一个池 （概念）  N个进程  哪个空闲  哪个就拿出来直接用   当进程用完后，会回到进程池
    Pools=multiprocessing.Pool(2)

    for i in range(10):
        #apply同步
        # Pools.apply(func=num,args=(i,))
        #apply_async异步
        Pools.apply_async(func=num,args=(i,))
    Pools.close()#进程池 不在接受任何新的任务了
    Pools.join()


    #多进程
    # processes=[]
    # for i in range(10):
    #     p1=multiprocessing.Process(target=num,args=(i,))
    #     processes.append(p1)
    #     p1.start()
    #
    # for i in processes:
    #     i.join()

    print('进程结束')