'''
带参数的 __init__()

思考：既然一个类可以创建多个对象，那么如何对不同的对象设置不同的初始化属性呢？
答：传参数
'''


class Washer():
    def __init__(self, width, height): # 添加两个准备传入数据的形参
        # 在类里面添加对象属性
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')


haier1 = Washer(100, 200)
haier1.print_info()

haier2 = Washer(300, 400)
haier2.print_info()
