

def add(a,b):
    try:
        return a+b

    except TypeError as e:
        print("错误！只能输入数字",e)
    finally: #一定会执行
        print("执行finally")

tmp=add(1,2)
print(tmp)