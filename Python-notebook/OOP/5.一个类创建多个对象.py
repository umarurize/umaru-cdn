'''
一个类创建多个对象

测试目标：
    1.一个类可以创建多个对象
    2.多个对象都调用函数时，self 地址是否相同
'''


class Washer():
    def wash(self):
        print('能洗衣服')
        print(self)


haier1 = Washer()
haier1.wash()

haier2 = Washer()
haier2.wash()

# 总结：两次返回的 self 地址不同，证明了一个类可以创建多个对象，因为不同的对象存储的内存地址是不同的


