'''
列表中的查找函数：
    1.index()
    2.count()
    -- 这两个和字符串的查找方式相同
    3.len() -- 访问列表长度，即列表中的数据个数
'''

# 1.index()
name_list = ['Tom', 'Lily', 'Rose']
print(name_list.index('Tom'))
# print(name_list.index('Toms')) -- 报错

# 2.count()
print(name_list.count('Tom')) # 返回1
print(name_list.count('Toms')) # 不存在则返回0

# 3.len()
print(len(name_list))