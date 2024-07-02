'''
三目运算符作用
化简简单的 if..else 逻辑
条件成立执行 if 表达式；条件不成立执行 else 表达式
'''
a = 1
b = 2

c = a if a > b else b
print(c)

# 需求：有两个变量，比较大小；如果变量1大于变量2，变量1-变量2；否则变量2-变量1
aa = 1
bb = 2

cc = aa - bb if aa > bb else bb - aa
print(cc)