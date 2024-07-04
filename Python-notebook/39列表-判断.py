'''
列表中常用的判断
    1.in -- 判断指定数据是否在某个列表序列，存在则返回 True；不在则返回 False
    2.not in -- 用法和 in 相反
'''

name_list = ['Tom', 'Lily', 'Rose']

# 1. in
print('Tom' in name_list)

# 2. not in
print('Tom' not in name_list) # False
print('Toms' not in name_list) # True

# 案例：查找用户输入的名字是否已存在
name = input('请输入你想要搜索的名字：')

if name in name_list:
    print(f'您输入的名字是{name}, 名字已存在')
else:
    print(f'您输入的名字是{name}, 名字不存在')