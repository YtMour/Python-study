# if else
#for while
#死循环 -- 结束条件
#break跳出循环
#contnue 继续循环

#while True:
for i in range(100):
    username=input("请输入用户名：")

    if username=="admin":
        print("登录成功")
        break
    else:
        print("用户错误,请检查并重新输入")

print("程序结束")