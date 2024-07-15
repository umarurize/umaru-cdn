'''
内置高阶函数
    1.map()：
    map(func, lst) -- 将传入的函数变量 func 作用到 lst 变量中的每个元素，并将组成的迭代器返回

    2.reduce()
    reduce(func, list) -- func 中必须包含2个参数，每次 func 的计算结果将继续和序列的下一个元素做累积计算
    注：reduce() 传入的参数 func 必须接收到2个参数

    3.filter()
    filter(func, lst) -- 用于过滤序列，过滤掉不符合条件的元素，返回一个 filter 对象
    如果需要转化为列表，可用 list() 来转换
'''


# 1.map()
# 需求：计算 list1 序列中各个数字的 2 次方
list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


result = map(func, list1)

print(result) # 返回 <map object at 0x000001BA311AE160> 迭代器，一个内存地址
print(list(result)) # 用 list() 转换函数，返回结果 [1, 4, 9, 16, 25]


# 2.reduce()
# 需求：计算 list2 序列中各个数字的累加和
import functools # 导入模块

list2 = [1, 2, 3, 4]


def func(a, b):
    return a + b


result1 = functools.reduce(func, list2)
print(result1) # 返回 10


# 3.filter()
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x % 2 == 0


result2 = filter(func, list2)
print(list(result2)) # 返回 [2, 4, 6, 8, 10]




