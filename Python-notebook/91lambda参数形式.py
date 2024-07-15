'''
lambda 参数形式
    1.无参数
    2.一个参数
    3.默认参数
    4.可变参数 *args
'''


# 1.无参数
fn1 = lambda: 100 # 无形参，只有返回值
print(fn1()) # 返回 100

# 2.一个参数
fn2 = lambda a: a # 形参 a，并返回 a
print(fn2('hello world')) # 返回 'hello world'

# 3.默认参数（缺省参数）
fn3 = lambda a, b, c=100: a + b + c # 默认参数 c=100；如果 c 没有传入实际数据，那么 c 默认为 c=100
print(fn3(10, 20)) # 返回 130，即 10+20+100
print(fn3(10, 20, 200)) # 返回 230

# 4.可变参数 *args（接收不定长的参数）
fn4 = lambda *args: args # 形参 *args 接收任意长度的形参，返回一个元组
print(fn4(10, 20, 30)) # 返回 (10, 20, 30)
print(fn4(1, 2, 3, 4)) # 返回 (1, 2, 3, 4)

# 5.可变参数 **kwargs（接收不定长的关键字参数）
fn5 = lambda **kwargs: kwargs
print(fn5(name='Python', age=20)) # 返回 {'name': 'Python', 'age': 20}
print(fn5(name='Python')) # 返回 {'name': 'Python'}
