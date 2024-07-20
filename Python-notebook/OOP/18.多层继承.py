'''
多层继承（即父类的属性和方法继承给子类，子类又作为父类，又把继承的属性和方法继承给下一个子类）

这种大于等于两层的继承关系称之为多层继承

需求延续：N年后，wch 老了，想要把所有技术传承给自己的徒弟
'''


# 1.师父类
class Master(object):
    def __init__(self):
        self.tech = '[古法煎饼果子方法]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


# 2.学校类
class School(object):
    def __init__(self):
        self.tech = '[技校煎饼果子方法]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


# 3.徒弟类
class Prentice(School, Master):
    def __init__(self):
        self.tech = '[独创煎饼果子方法]'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.tech}制作煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        print(f'运用{self.tech}制作煎饼果子')

    def make_school_cake(self):
        School.__init__(self)
        print(f'运用{self.tech}制作煎饼果子')


# 4.徒孙类
class Tusun(Prentice):
    pass


wch_son = Tusun()

wch_son.make_cake()

wch_son.make_master_cake()

wch_son.make_school_cake()
