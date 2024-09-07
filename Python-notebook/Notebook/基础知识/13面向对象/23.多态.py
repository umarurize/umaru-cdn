'''
多态 -- 多态指的是一类事物有多种形态，在 Python 中抽象为（一个类有多个子类，因而多态的概念依赖于继承）

    1.定义：多态是一种使用对象的方式，子类重写父类方法；调用不同子类对象的相同父类方法，可以产生不同的执行结果

    2.优点：调用灵活，有了多态，更容易编写出通用代码，做出通用的编程，以适应需求的不断变化

    3.实现步骤：
        - 定义父类，提供公共方法
        - 定义子类，重写父类方法
        - 传递子类对象给调用者，可以看到不同子类的执行效果不同
'''


class Dog(object):
    def work(self):
        print('指哪儿打哪儿...')


class ArmyDog(Dog):
    def work(self): # 同名方法，子类覆写父类方法
        print('追击敌人...')


class DrugDog(Dog):
    def work(self):
        print('缉查毒品...')


class Police(object):
    def work_with_dog(self, dog):
        dog.work()


dog = Dog()
dog1 = ArmyDog()
dog2 = DrugDog()
wch = Police()

wch.work_with_dog(dog1)

wch.work_with_dog(dog2)

wch.work_with_dog(dog)