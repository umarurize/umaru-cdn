'''
字典的循环遍历
    1.遍历字典的 key
    2.遍历字典的 value
    3.遍历字典的 item（即 key:value，键值对）
'''

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 1.遍历字典的 key
# 首先要查找到字典中所有的 key -- keys()
for key in dict1.keys():
    print(key)

# 2.遍历字典中的 value
for value in dict1.values():
    print(value)

# 3.遍历字典中的 item
for item in dict1.items():
    print(item) # 返回的是元组....元组的数据1是 key；元组的数据2是 value

'''
字典的键值对拆包
'''
for key, value in dict1.items():
    print(f'{key} = {value}')