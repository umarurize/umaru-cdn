'''
字符串操作符
    运算符     举例      描述
    +         x + y     字符串 x 与字符串 y 连接
    *         x * y     复制 y 次字符串 x
    in        x in y    如果 x 是 y 的子串，返回 True，否则返回 False
'''

str1 = 'Hello'
str2 = 'World'
str3 = 'How are you?'
print(str1 + str2) # return HelloWorld
print(str1 * 2) # return HelloHello
print(str1 in str2) # return False
print('are' in str3) # return True