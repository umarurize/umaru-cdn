'''
2.多继承
    思考：wch 是个爱学习的好孩子，想学习更多的煎饼果子技术。于是，报班学习了更多煎饼果子技术。

    所谓多继承是一个类同时继承了多个父类
'''


# 师父类
class Master(object):
    def __init__(self):
        self.tech = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


# 学校类
class School(object):
    def __init__(self):
        self.tech = '[技校煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


# 徒弟类
class Prentice(School, Master): # 当一个类有多个父类时，默认使用第一个父类的同名属性和方法
    pass


wch = Prentice()
print(wch.tech)
wch.make_cake()