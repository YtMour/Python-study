
#封装思想
#参数   属性
#函数   方法
class Human:
    def __init__(self, name):
        self.name = name
        print("self->", self)

    def speak(self):
        print("Human-----》"+self.name)

#实例化 init new
h1=Human("H1")
print(h1.name)
h1.speak()

h2=Human("H2")
print(h2.name)
h2.speak()