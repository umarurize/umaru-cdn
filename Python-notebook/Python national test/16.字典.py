'''
字典
    1.字典的定义
    2.字典的索引
    3.字典的操作
'''


'''
1.字典的定义
    - 字典类型数据主要以 '键值对' 的形式存储
    - 格式：{<key1>: <value1>, <key2>: <value2>}
'''
first_dict1 = {'name': 'LX', 'gender': 'male', 'age': 18}
print(type(first_dict1)) # return <class 'dict'>


'''
2.字典索引
    - 通过键来寻找字典中对应的值，类似查汉语字典的过程
    - 语法：<字典变量>[索引]
'''
# 2.1 通过键查找对应的值
print(first_dict1['gender']) # return male
print(first_dict1['age']) # return 18

# 2.2 通过键修改值
second_dict1 = {'name': 'LX', 'gender': 'male', 'age': 18}
second_dict1['name'] = 'LYT'
print(second_dict1) # return {'name': 'LYT', 'gender': 'male', 'age': 18} -- 可以看到 'name' 的值被成功修改

# 2.3 增加键值对
second_dict1['student_id'] = 12
print(second_dict1) # return {'name': 'LYT', 'gender': 'male', 'age': 18, 'student_id': 12}


'''
3.字典常用操作函数
    函数                    描述
    len(d)                  返回字典 d 中元素的个数
    min(d)                  返回字典 d 中键的最小值
    max(d)                  返回字典 d 中键的最大值
    in                      元素的键在字典中，返回 True；不在则返回 False
    not in                  元素的键在字典中，返回 False；不在则返回 True
'''
third_dict1 = {'name': 'LX', 'gender': 'male', 'age': 18}
print(len(third_dict1)) # return 3 -- 返回了 third_dict1 中元素（键值对）的个数
print(max(third_dict1)) # max() 用来输出字典中键的最大值，如果不是数字，就比较字母顺序的最大值

print('name' in third_dict1) # 返回 True


'''
4.字典常用操作方法
    操作方法                  描述
    d.keys()                 返回所有键的信息
    d.values()               返回所有值的信息
    d.items()                返回所有的键值对
    d.get(key, default)      键存在则返回相应值，否则返回 default
    d.pop(key, default)      键存在则删除相应键值对，并返回相应值，否则返回 default
    d.popitem()              随机从字典中取出一个键值对，以元组 (key, value) 形式返回，同时将该键值对从字典中删除
    d.clear()                清空字典                       
'''
forth_dict1 = {'name': 'LX', 'gender': 'male', 'age': 18}

# 4.1 .keys()
print(forth_dict1.keys()) # return dict_keys(['name', 'gender', 'age']) -- 即返回字典中所有键的信息

# 4.2 .values()
print(forth_dict1.values()) # return dict_values(['LX', 'male', 18])

# 4.3 .items()
print(forth_dict1.items()) # return dict_items([('name', 'LX'), ('gender', 'male'), ('age', 18)])

# 4.4 .get(key, default)
print(forth_dict1.get('name')) # return LX
print(forth_dict1.get('stu_id', '没有此信息')) # return 没有此信息 -- 如果不写第二个参数，不存在则返回 None
# print(forth_dict1['stu_id']) -- 没有该键则会报错

# 4.5 .pop(key, default)
forth_dict2 = {'name': 'LX', 'gender': 'male', 'age': 18}
print(forth_dict2.pop('name')) # return LX -- 即被删除键对应的值
print(forth_dict2) # return {'gender': 'male', 'age': 18} -- 说明键值对 'name': 'LX' 被删除
print(forth_dict2.pop('stu_id', '没有此信息')) # return 没有此信息，这点和 .get() 功能一样的

# 4.6 .popitem()
print(forth_dict2.popitem()) # return ('age', 18) -- 证明随机删除了 'age': 18 键值对


'''
5.字典配合 for 循环
'''
fifth_dict1 = {'name': 'LX', 'gender': 'male', 'age': 18}
for i in fifth_dict1: # 也可以是 for i in fifth_dict1.keys():
    print(i, end = '\t') # return 'name	gender	age	' -- 这里遍历的是字典中所有的键

print('')

for i in fifth_dict1: # 也可以是 for i in fifth_dict1.values():
    print(fifth_dict1[i], end = '\t') # return 'LX	male	18	' -- 遍历字典中所有的值

print('')

for i in fifth_dict1.items():
    print(i, end = '\t') # return '('name', 'LX')	('gender', 'male')	('age', 18)	' -- 遍历字典中所有的键值对，每个元素都是一个元组

print('')

# 键值对拆包
for k, v in fifth_dict1.items():
    print(k, v)





