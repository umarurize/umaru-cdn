'''
字典的语法特点：
    1.符号为大括号
    2.数据为键值对形式出现
    3.1个字典当中可以存储多个键值对，各个键值对之间要用逗哈隔开

创建字典：
    1.有数据字典
    2.空字典
'''

# 1.创建字典 需求：name 的值是 Tom；age 的值是 28；gender 的值是 男
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'} # 键值对 key: value，其中 name、age、gender 称为 key；Tom、20、男 称为 value
print(dict1)
print(type(dict1))

# 2.创建空字典
dict2 = {} # 直接赋值一个空字典
dict3 = dict() # 用 dict() 函数创建空字典
print(type(dict3))


