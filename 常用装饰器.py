

# class YT:
#     def __init__(self):
#         self.qq="123456"
#     @property   #把类方法   转换为  类属性方式获取
#     def yt_qq(self):
#         return self.qq
#
#     @yt_qq.setter
#     def yt_qq(self,value):
#         self.qq = value
#     @yt_qq.deleter
#     def yt_qq(self,value):
#         del self.qq
#
# x=YT()
# x.yt_qq=1
# del x.yt_qq
# print(x.yt_qq)

# class YT:
#     var =1
#     def __init__(self):
#         self.qq="123456"
#     @classmethod   #类方法   表示属于类  不属于示例
#     def yt_qq(cls):
#         print(cls)
#         print(YT.var)
# YT.yt_qq()

import random
class YT:
    var =1
    def __init__(self):
        self.qq="123456"
    @staticmethod   #静态方法  当前方法 不属于类  是一个单独的函数
    def get_num():
        print(random.random())

YT.get_num()