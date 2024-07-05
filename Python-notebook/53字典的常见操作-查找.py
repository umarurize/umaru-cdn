'''
字典 -- 数据查找
方式：
    1.key 值查找
    2.函数方式：
        2.1 get() -- 字典序列.get(key, 默认值)
        2.2 keys() -- 字典序列.keys() -- 遍历字典中的所有 key
        2.3 values() -- 字典序列.values() -- 遍历字典中所有的 value
        2.4 items() -- 字典序列.items() -- 遍历字典中所有可迭代的对象，并返回元组，元组数据1是 key，元组数据2是 value
'''

# 1.key值查找
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

print(dict1['name']) # 返回 Tom，查找成功

# 2.函数查找
# 2.1 get() -- 字典序列.get(key, 默认值)
# 如果当前查找的 key 不存在，则返回第二个参数（默认值）；如果省略第二个参数，则返回 None
print(dict1.get('name')) # Tom

print(dict1.get('id', 110)) # 因为 id 这个 key 不存在，所以返回第二个参数 110

print(dict1.get('id')) # None，因为 id 这个 key 不存在，并且没有第二个参数

# 2.1 keys()
print(dict1.keys()) # 相当于遍历了 key，返回可迭代对象（即可用 for 遍历的对象）

# 2.2 values()
print(dict1.values()) # 同2.1

# 2.3 items()
print(dict1.items()) # 遍历字典中所有可迭代的对象，并返回元组，元组数据1是 key，元组数据2是 value




