#学生管理系统
#姓名 性别 专业 学分
class System:
    def __init__(self):
        print('学生管理系统Version0.1')
        self.students={}
        print('1.添加学生信息')
        print('2.更新学生信息')
        print('3.删除学生信息')
        print('4.列出学生信息')
        print('5.退出系统')

    def start(self):
        while True:
            args=int(input('请输入序号：'))
            if args==1:
                name=input('请输入学生姓名：')
                gender = input('请输入学生性别：')
                major = input('请输入学生专业：')
                score = input('请输入学生学分：')
                self.add_student(name,gender,major,score)
            elif args==2:
                name = input('请输入学生姓名：')
                self.update_student(name)
            elif args==3:
                name = input('请输入学生姓名：')
                self.del_student(name)
            elif args==4:
                self.list_students()
            elif args==5:
                print('再见！')
                exit(0)


    def add_student(self,name,gender,major,score):
        stus=self.students.get(name,None)
        if not stus:
            self.students[name]={"性别":gender,'专业':major,"学分":score}
            print('已添加{}'.format(name))
        else:
            print('已找到学生:{} 信息:{}'.format(name,stus))
            result=input('是否进行信息更新？(是/否):')
            if result=='是':
                args = input('请输入要修改的参数(性别/专业/学分):')
                if args=='性别':
                    self.students[name]['性别']=args
                elif args=='专业':
                    self.students[name]['专业'] = args
                elif args=='学分':
                    self.students[name]['学分'] = args
            print('信息更新完毕！')

    def del_student(self,name):
        stus=self.students.get(name,None)
        if not stus:
            print('该学生不存在！')
        else:
            del self.students[name]
            print('学生 {} 已被删除！'.format(name))

    def update_student(self,name):
        stus = self.students.get(name, None)
        print('已找到学生:{} 信息:{}'.format(name, stus))
        args = input('请输入要修改的参数(性别/专业/学分):')
        if args == '性别':
            tmp=input('请输入新的性别：')
            self.students[name]['性别'] = tmp
        elif args == '专业':
            tmp = input('请输入新的专业：')
            self.students[name]['专业'] = tmp
        elif args == '学分':
            tmp = input('请输入新的学分：')
            self.students[name]['学分'] = tmp
        print('信息更新完毕！')

    def list_students(self):
        if self.students=={}:
            print('暂无信息')
        else:
            for index,stu in enumerate(self.students.items()):
                print('序号：{} 信息：{}'.format(index,stu))

if __name__ == '__main__':
    s=System()
    s.start()