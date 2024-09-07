'''
子类重写父类同名属性和方法

需求延续：wch 掌握了师父和技校的煎饼果子技术后，自己钻研出了独门配方。
'''


# 1.师父类
class Master(object):
    def __init__(self):
        self.tech = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


# 2.学校类
class School(object):
    def __init__(self):
        self.tech = '[技校煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


# 3.徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.tech = '[独创煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


wch = Prentice()

print(wch.tech)

wch.make_cake()

# 总结：如果子类和父类拥有同名属性和方法，子类对象在调用时，调用的是子类的同名属性和方法

# __mro__ 顺序代码测试
print(Prentice.__mro__)