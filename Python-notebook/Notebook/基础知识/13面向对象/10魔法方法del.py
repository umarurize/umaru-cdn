'''
魔法方法 __del__()

当删除对象时，Python 解释器会默认调用 __del__() 方法
'''


class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __del__(self):
        print(f'{self}对象已经删除')


haier = Washer(100, 200)

# __del__() 会自动调用，就不需要额外书写 del haier 来删除对象
