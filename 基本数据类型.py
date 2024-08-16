# str int float bool list dict tuple set
#布尔值  真假 1 0
#字符串 和引号无关
str_a = 'yt'
str_b = "YT"
str_c = """YYY"""
print(str_a)
print(str_b)
print(str_c)

int_a=123456
float_=3.14
print(int_a)
print(float_)
print(type(int_a))
print(type(float_))

bool_a=True
print(bool_a,type(bool_a))
print(1==1)
print(1==0)
print(0==0)

#list
list_a=[1,2,3,4.11,"YT",[123,"yyy"]]
print(list_a)
print(list_a[5])
list_a[0]="qwe"
print(list_a)
del list_a[0]
print(list_a)

#字典   key   value
dict_a ={"yt":100,"yyy":200,"test":[1,2,3]}
print(dict_a)
print(dict_a["yt"])
dict_a["yt"]=300
print(dict_a)
del dict_a["yt"]
print(dict_a)

#tuple 元组   无法更改  类似列表
tuple_a=(1,2,"yt")
print(tuple_a,type(tuple_a))
print(tuple_a[1])


#set 集合 过滤
set_a=set((1,1,1,2,2,3,4,4,4,5,5,6,9,7,"yt","yt"))
print(set_a)

list_b=[1,2,3,4,4,5,5,55,6,6,6,7,7,7]
set_b=set()
for i in list_b:
    set_b.add(i)
    print(set_b)