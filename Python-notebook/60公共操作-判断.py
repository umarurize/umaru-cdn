'''
公共操作之判断：
    1.in -- 判断元素是否存在 -- 字符串、列表、元组、字典
    2.not in -- 与 in 的用法完全相反
返回的值都是 bool 型
'''

str1 = 'abcd'
list1 = [10, 20, 30, 40]
t1 = (100, 200, 300, 400)
dict1 = {'name': 'Python', 'age': 20}
# 1. 需求：判断字符a是否存在
print('a' in str1) # True

print('a' not in str1) # False

print(10 in list1) # True

print(10 not in list1) # False

print(100 in t1) # True

print(100 not in t1) # False

print('name' in dict1) # True

print('name' not in dict1) # True

print('name' in dict1.keys()) # True

print('name' in dict1.values()) # False -- 因为 name 是 key，并不是 value

