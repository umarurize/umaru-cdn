'''
面向对象 -- 继承
    学习路线：
        1.继承的概念
        2.单继承
        3，多继承
        4.子类重写父类的同名属性和方法
        5.子类调用父类的同名属性和方法
        6.多层继承
        7.super()
        8.私有属性和私有方法
'''


'''
拓展 -- 经典类和新式类
    1.经典类
    class 类名：
        代码
        ....
    
    2.新式类
    class 类名(object) -- 默认式 object，但是也可以修改想要继承的类
        代码
        ...
    
    以后的工作场景中，都是新式类
'''


'''
继承入门
    Python 面向对象的继承指的是多个类之间的所属关系，即子类默认继承父类的所有属性和方法
    
    继承分类：
        1.单继承
        2.多继承
'''


class A(object):
    def __init__(self):
        self.num = 1

    def print_info(self):
        print(self.num)


class B(A):
    pass


result = B()
result.print_info() # 返回 1，继承成功

# 补充：在 Python 当中，所有类默认继承 object 类，object 类是顶级类（基类）；其它子类叫做派生类


'''
1.单继承
    思考：一个煎饼果子老师傅，在煎饼果子界摸爬滚打多年，研发了一套精湛的摊煎饼果子的技术。师父要把这套技术传授给他的唯一最得意的徒弟。
    
    分析：徒弟是不是要继承师父的所有技术？
'''


# 师父类
class Master(object):
    def __init__(self):
        self.tech = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.tech}制作煎饼果子')


# 徒弟类
class Prentice(Master):
    pass


wch = Prentice()
print(wch.tech) # 返回 [古法煎饼果子]
wch.make_cake()









