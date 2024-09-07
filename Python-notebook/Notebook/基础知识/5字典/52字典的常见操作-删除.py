'''
字典 -- 删除数据操作
函数:
    1.del() 或 del -- 删除字典或删除字典中指定的键值对
    2.clear() -- 清空字典
'''

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 1.del
# del(dict1)
# print(dict1) -- 报错 not found

del dict1['name']
print(dict1)

# 2.clear()
dict2 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict2.clear()
print(dict2)