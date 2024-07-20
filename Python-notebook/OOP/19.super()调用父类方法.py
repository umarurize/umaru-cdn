'''
super() 调用父类方法
'''


class Master(object):
    def __init__(self):
        self.tech = '[古法煎饼果子方法]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


# 2.学校类
class School(Master):
    def __init__(self):
        self.tech = '[技校煎饼果子方法]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')
        super().__init__()
        super().make_cake()


# 3.徒弟类
class Prentice(School):
    def __init__(self):
        self.tech = '[独创煎饼果子方法]'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.tech}制作煎饼果子')

    def make_old_cake(self):
        # 方法1：
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        #方法2：super(当前类名, self).函数()
        super(Prentice, self).__init__()
        super(Prentice, self).make_cake()


wch = Prentice()

wch.make_cake()

wch.make_old_cake() # 成功调用两个父类方法

print(Prentice.__mro__)

'''
小结：
老式子类调用父类同名属性和方法的缺点
    1.如果父类名变动，子类调用时也要随之变动
    2.如果调用父类多（例如100个），明显会造成代码冗余的现象
'''