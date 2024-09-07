'''
获取和修改私有属性值：
    在类外获取私有属性值，会面临报错，但如果想要修改私有属性值，该怎么办？

    在 Python 中，一般定义函数名 get_xx 用来获取私有属性，定义 set_xx 用来修改私有属性值
'''


class Master(object):
    def __init__(self):
        self.tech = '[Old method]'
        self.__money = 2000

    def __info_print(self):
        print(self.__money)

    def make_cake(self):
        print(f'use {self.tech} to make cake')

    def get_money(self):
        return self.__money

    def set_money(self):
        self.__money = 500


class Prentice(Master):
    pass


wch = Prentice()

print(wch.get_money()) # return 2000

print(wch.set_money()) # return 500

wch.info_print()