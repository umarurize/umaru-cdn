'''
类属性和实例属性

'''


'''
A.类属性
    1.类属性就是类对象所拥有的属性，它被该类的所有实例对象所共有
    2.类属性可以使用类对象或实例对象访问
'''


class Dog(object):
    tooth = 10


dog1 = Dog()
dog2 = Dog()

print(Dog.tooth) # return 10 -- 使用类对象访问类属性

print(dog1.tooth) # return 10 -- 使用实例对象访问类属性
print(dog2.tooth) # return 10


'''
小结 -- 类属性的优点
    1.记录的某项数据始终保持一致时，则定义类属性
    2.实例属性会为每个对象单独开辟一份内存空间，用来记录数据；类属性则为全类所共有，仅占一部分内存，节省了计算机空间
    
'''


'''
B.修改类属性
    类属性只能通过类对象修改，不能通过实例对象修改；如果通过实例对象修改类属性，那意味着创建了一个类属性
'''
# 修改类属性
Dog.tooth = 12

print(Dog.tooth) # return 12
print(dog1.tooth) # return 12
print(dog2.tooth) # return 12

# 测试通过实例对象修改类属性会怎样
dog1.tooth = 20
print(dog1.tooth) # return 20 -- 实际上是创建了一个新的同名实例属性
print(Dog.tooth) # return 12 -- 类属性没有的到修改
print(dog2.tooth) # return 12
