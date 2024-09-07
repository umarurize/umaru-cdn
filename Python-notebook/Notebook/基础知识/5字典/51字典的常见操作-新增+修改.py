'''
新增的数据必须是一个键值对
书写：
    字典序列['key'] = 值
注意：
    1.字典不支持下标
    2.新增数据时，如果 key 存在则修改 key 对应的值；反之直接新增该键值对
    3.字典为可变类型
'''

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 新增数据
# 需求：增添 id 的值是 110
dict1['id'] = 110
print(dict1)

dict1['name'] = 'Rose'
print(dict1)

