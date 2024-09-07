str1 = 'abcdefg'
list1 = [10, 20, 30, 40, 50]
t1 = (10, 20, 30, 40, 50)
s1 = {10, 20, 30, 40, 50}
dict1 = {'name': 'Tom', 'age': 18}

# 1.len()
print(len(str1)) # 返回7，str1 中有7个字符数据

print(len(list1)) # 返回5

print(len(t1)) # 返回5

print(len(s1)) # 返回5

print(len(dict1)) # 返回2，dict1 中有2个键值对（key:value）

# 2.del() 或 del 目标
del str1
# print(str1) --报错 not found

# del list1 -- 效果同上

del list1[0]
print(list1) # 返回 [20, 30, 40, 50]

# del tuple 和 del tuple[] 的用法和 list 相同

# del dict1 -- 效果同上

del dict1['name']
print(dict1) # 返回 {'age': 18}

# 3.max() 和 min()
str2 = 'abcdefg'
list2 = [10, 20, 30, 40, 50]

# 2.1 max()
print(max((str2))) # 返回 g
print(max(list2)) # 返回 50
# tuple 和 dict 的用法同上

# 2.2 min()
print(min((str2))) # 返回 a
print(min(list2)) # 返回 10
# tuple 和 dict 的用法同上