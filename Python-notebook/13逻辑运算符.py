'''
1. and 代表与（且），如果两者都为 True 则返回 True；如果两者任何一个为 False 则返回为 False
2. or 代表或，只要两者有一个为 True 则返回 True；如果两者都为 False，则返回为 False
3. not 代表非，取相反
'''

# 1. and
a = 0
b = 1
c = 2
print(a < b and c > b)
print(a < b and c < b)

# 2. or
print(a < b or c < b)
print(a > b or c < b)

# 3. not
print(not False)
print(not c > b)

'''
工作场景中的书写习惯
'''
#加小括号避免歧义
print((a < b) and (c > b))

'''
逻辑运算符拓展
'''
# 1. and 运算符中，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
print(a and b)
print(b and c)

# 2. or 运算符中，只有所有值为0结果才为0，否则结果为第一个非0数字
print(a or a)
print(b or c)