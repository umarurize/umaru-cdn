'''
私有权限
    1.定义私有属性和方法：
        在 Python 中，可以为实例属性和方法设置私有权限，即设置某个实例的属性或方法不继承给子类

    2.设置方法：
        在属性名和方法名前面加两个下划线

需求延续：wch 把技术传承给自己徒弟时，不想把钱继承给徒弟，这时候就要把钱这个属性设置为私有属性

'''


class Master(object):
    def __init__(self):
        self.tech = '[Old method]'

    def make_cake(self):
        print(f'use {self.tech} to make cake')


class School(object):
    def __init__(self):
        self.tech = "[School's method]"

    def make_cake(self):
        print(f'use {self.tech} to make cake')


# 3.徒弟类
class Prentice(Master, School):
    def __init__(self):
        self.tech = '[Personal method]'
        self.__money = 2000

    def make_cake(self):
        self.__init__()
        print(f'use {self.tech} to make cake')

    def __info_print(self):
        print(self.__money)

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 4.徒孙类
class Tusun(Prentice):
    pass

wch_son = Tusun()

wch_son.make_cake()

wch_son.info_print() # error





