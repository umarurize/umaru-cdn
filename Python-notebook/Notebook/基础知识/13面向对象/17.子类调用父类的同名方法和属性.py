'''
子类调用父类的同名方法和属性

需求延续：很多顾客除了想吃独门配方的煎饼果子，也想吃古法配方煎饼果子和技校配方煎饼果子
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
        # 如果不加自己的初始化，那么子类的属性值会被上次调用的父类属性值覆盖
        self.__init__()
        print(f'运用{self.tech}制作煎饼果子')

    # 子类调用父类的同名属性和方法 -- 其实就是把父类的同名属性和方法再次封装即可
    def make_master_cake(self):
        # 再次调用初始化，原因是想再次调用父类的属性，而父类的属性在初始化中
        Master.__init__(self)
        # 再次调用父类的方法 -- 父类名.函数()
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


wch = Prentice()

wch.make_cake() # 返回运用[独创煎饼果子配方]制作煎饼果子

wch.make_master_cake()

wch.make_school_cake()

