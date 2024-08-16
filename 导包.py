

"""
官方包  自带了  直接导入
三方包  额外下载  第三方团队 或 个人 开发
"""

#import random
#只导入需要的  减少程序体积    也可以 as设置别名  防止与自己的函数冲突
# from random import randrange,seed
# #random.seed(100)
# seed(100)
# num= randrange(0,10)
# while True:
#     mynum=int (input("请输入你猜的数字："))
#
#     if mynum==num:
#         print("恭喜猜对！")
#         break
#     else:
#         print("回答错误")
#         if mynum>num:
#             print("数字大了")
#         else:
#             print("数字小了")


import requests
img = requests.get("https://avatars.githubusercontent.com/u/92254553?v=4")
print(img.content)
with open('img.jpg', 'ab') as f:
    f.write(img.content)