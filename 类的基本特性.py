#继承   __ 下划线开头代表私有
class Human:
    def __init__(self, name):
        self.name = name
        print("self->", self)

    def speak(self):
        print("Human-----》"+self.name)
    def __test(self):
        print("测试")

class YT(Human):
    def __init__(self, name):
        self.yt = name
        super(YT, self).__init__(name)
    def run(self):
        print("正在跑")

    def speak(self):
        print("Yt-----》"+self.name)

y1=YT("yt")
y1.speak()
y1.run()