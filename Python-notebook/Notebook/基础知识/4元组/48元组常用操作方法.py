'''
元组数据不支持修改，因此只支持查找
查找方式：
    1.按下标查找数据
    2.index() -- 查找某个数据，如果数据存在，则返回对应的下标；否则报错
    3.count() -- 统计某个数据在元组中出现的次数
    4.len() -- 统计元组中数据的个数
'''

# 1.下标
t1 = ('aa', 'bb', 'cc', 'dd')
print(t1[0])

# 2.index()
print(t1.index('bb')) # 返回1，即数据'bb'在元组中的下标

# 3.count()
print(t1.count('aa')) # 返回1，即数据'aa'在元组中出现的次数
print(t1.count('ee')) # 返回0，即数据'bb‘在元组中不存在

# 4.len()
print(len(t1)) # 返回4，即元组中所以数据的个数



