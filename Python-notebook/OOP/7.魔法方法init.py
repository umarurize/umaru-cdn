'''
魔法方法

在面向对象中，__xx__() 的函数叫做魔法方法，指的是具有特殊功能的函数
'''


'''
魔法方法__init__()

    思考：洗衣机的宽度高度是与生俱来的属性，可不可以在生产过程中就赋予这些属性呢？
    答：可以

    作用：初始化对象

    注意事项：
        1.__init__() 方法，在创建一个对象时默认被调用，不需要手动调用
        2.__init__(self) 中的 self 参数，不需要手动传递，Python 解释器会自动把当前的对象引用过去传递
'''


class Washer():
    def __init__(self):
        # 类里面添加对象属性
        self.width = 400
        self.height = 300

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')


haier = Washer()

haier.print_info()




