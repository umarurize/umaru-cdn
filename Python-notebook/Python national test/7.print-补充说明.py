'''
print 输出不换行
    print(<输出内容>, end = <输出的结尾（可自定义）>)
'''

# 1.默认输出方式
a = 1
b = 2
print(a)
print(b) # 可见 Python 默认是换行输出的

# 2.不换行输出
print(a, end = '')
print(b) # 不换行输出，两行输出的显示效果是 12

# 3.自定义输出结尾
print(a, end = '%')
print(b) # 两行输出的显示效果是 1%2