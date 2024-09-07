'''
魔法方法 __str__()

当使用 print 输出对象时，默认打印对象的内存地址。如果类中定义了__str__方法，那么就会打印从这个方法中 return 的数据。

'''


class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return '这是 haier 洗衣机的说明书'

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')


haier = Washer(200, 300)

haier.print_info()

print(haier) # 这里返回的就不是对象内存的地址了

