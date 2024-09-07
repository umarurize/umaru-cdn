'''
类方法
    1.特点：
    需要用装饰器 @classmethod 来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以 cls 作为第一个参数

    2.使用场景：
        2.1 当方法中需要使用类对象（如访问私有类属性）时，需要定义类方法
        2.2 类方法一般和类属性配合使用
'''


class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


dog1 = Dog()

result = dog1.get_tooth()

print(Dog.get_tooth())

print(result) # return 10

