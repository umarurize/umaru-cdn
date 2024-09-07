'''
增加，增加数据到列表中
函数：
    1. append() -- 在列表结尾追加数据 -- 语法：列表序列.append(数据)、
    2. extend() -- 在列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表 -- 语法：列表序列.extend(数据)
    3.insert() -- 在指定位置新增数据 -- 语法：列表序列.insert(位置下标, 数据)
'''

# 1.append()
name_list = ['Tom', 'Lily', 'Rose']
name_list.append(['lx', 'lfq']) # 如果追加的是一个列表序列，那会追加整个序列到列表的结尾
print(name_list) # 列表不同于字符串，是可变的数据

# 2.extend()
name_list1 = ['Tom', 'Lily', 'Rose']
name_list1.extend(['lx', 'lfq']) # 如果追加的是一个列表序列，那会将追加的序列分别拆开，再逐一追加
print(name_list1)

name_list2 = ['Tom', 'Lily', 'Rose']
name_list2.extend('lx') # 不同于 append，追加字符串，extend 也会将其逐个拆开成单个字符，再追加
print(name_list2)

# 3.insert
name_list2 = ['Tom', 'Lily', 'Rose']
name_list2.insert(1, 'aaa') # 加在了位置下标1的前面
print(name_list2)


