
#循环时计数
li=['yt','yt1','yt2']

for num,item in enumerate(li):
    print(num+1,item)


#多个序列打包循环
#多个序列  进行同时循环打印
li=[1,2,3,4,5]
li2=[10,11,12,13,14]

for a,b in zip(li,li2):
    print(a,b)