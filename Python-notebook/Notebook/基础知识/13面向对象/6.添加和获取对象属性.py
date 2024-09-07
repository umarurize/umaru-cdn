'''
添加和获取对象属性

属性：
    1.属性即特征，比如：洗衣机的宽度、高度、重量...
    2.对象属性既可以在类外面添加和获取，也可以在类里面添加和获取
'''


'''
1.类外面添加对象属性
    语法：对象名.属性名 = 值
    例如：haier1.width = 500；haier1.height = 800
'''


class Washer():
    def wash(self):
        print('洗衣服')


haier1 = Washer()

# 类外面添加对象属性
haier1.width = 500
haier1.height = 800

print(f'洗衣机的宽度是{haier1.width}cm，高度是{haier1.height}cm')


'''
2.类里面获取对象属性
    语法：self.属性名
'''


class Washer1():
    def print_info(self):
        # 类里面获取对象属性
        print(f'haier2洗衣机的宽度是{self.width}')
        print(f'haier2洗衣机的高度是{self.height}')


haier2 = Washer1()

haier2.width = 300
haier2.height = 200

haier2.print_info()