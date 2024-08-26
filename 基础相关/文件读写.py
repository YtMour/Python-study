
"""
w 写入  如果文件不存在，就创建
r 读取  读取文件内容
a 追加  把内容写入文件末尾  不存在就闯进啊， 存在就追加写入
b 二进制 写入视频，音频，图片之类的



f=open('yt.txt','w',encoding='utf-8')
f.write(line)
f.close()
不关闭就会导致内存泄露

with 自开合
"""

line="yt123456"
with open('yt.txt','w',encoding='utf-8') as f:
    f.write(line)


with open('yt.txt','r',encoding='utf-8') as f:
    content=f.read()
    print(content)