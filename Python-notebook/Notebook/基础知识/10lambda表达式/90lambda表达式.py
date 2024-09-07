'''
lambda 表达式
    1.lambada 的应用场景：
        如果一个函数有一个返回值，并且只有一句代码，那么可以用 lambada 简化
        当书写 lambda函数时，内存会开辟一个新的空间来存储
        lambda 能节省计算机和服务器的占用

    2.lambda 语法：
        lambda 参数列表 : 表达式
        lambda 表达式的参数可有可无，函数的参数在 lambda 表达式中完全适用
        lambda 表达式能接收任何数量的参数，但只能返回一个表达式的值
'''


# 1.lambda 快速入门
# 需求：函数，返回值 100
# 1.1 函数实现
def fn1():
    return 100


result = fn1()
print(result)


# 1.2 lambda 实现
fn2 = lambda: 100
print(fn2) # 返回 <function <lambda> at 0x00000235586CDC80>，因为 lambda 又叫匿名函数，所以返回的是函数代码（内存地址）

print(fn2()) # 调用 fn2() 函数，返回 100


# 2.lambda 实例
# 需求：计算 a + b
# 2.1 函数实现
def add_num(a, b):
    return a + b


result = add_num(1, 2)
print(result) # 返回 3


# 2.2 lambda 函数实现
fn3 = lambda a,b: a + b
print(fn3(1, 2)) # 返回 3

