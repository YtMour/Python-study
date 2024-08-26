

#高阶函数  -- 把函数 作为 参数
#计时装饰器 -- 计算函数执行时间
#参数是函数  返回内部函数  内部函数里边调用函数(传递参数)

import time
def Timer(func):
    start = time.time()
    def inner(*args, **kwargs):
        print('传递的参数：',*args,**kwargs)
        func(*args, **kwargs)
        end = time.time()
        print("耗费时间：",end-start)

    return inner

@Timer
def test(a,b,c):
    for i in range(1000):
        print(i)

test(1,2,3)
