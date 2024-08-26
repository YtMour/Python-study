
#with
#enter进入时会做什么   exit退出时会做什么
#__enter__ 相当于 as重命名后的
class File:
    def __init__(self, filename):
        self.file = open(filename,'r',encoding='utf-8')
    def __enter__(self):
        print('enter File')
        return self
    def __exit__(self, type, value, traceback):
        print('exit File')
        self.file.close()

    def read(self):
        return self.file.read()

# x=File('yt.txt')
# print(x.read())
with File('yt.txt') as f:
    print(f.read())