'''
运算符乘号：
    * -- 复制 -- 支持字符串、列表、元组
例如 a * 10 即复制10遍
'''

str1 = 'a'
list1 = ['hello']
t1 = ('world',) # 元组中存放单个数据时，

print(str1 * 5) # 输出 aaaa，成功复制5遍

print('-' * 5) # 输出 -----

print(t1 * 5) # 输出 ('world', 'world', 'world', 'world', 'world')

