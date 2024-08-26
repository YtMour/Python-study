

class YT:
    def __call__(self, *args, **kwargs):
        # print("call 被调用",args, kwargs)
        print("call 被调用",*args, *kwargs)


def hello(name,*args, **kwargs):
    print("hello",name)
    print("其余参数",args)
    print("键值对",kwargs)

hello('yt',30,test="hello world")


x=YT() #实例化
print(x)
x(1,2,3,'yt',name='yt')