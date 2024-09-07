'''
判断无非是判断 True or False，返回的值是 bool 型
函数：
    1.startswith(子串, 开始位置下标, 结束位置下标) -- 检查字符串是否以指定子串开头，是则返回 True；否则返回 False
    设置开始、结束位置下标，是为了在指定范围内查找
    2.endswith() -- 用法同上
'''

# 1.startswith()
mystr = 'hello world and itcast and itheima and Python'

print(mystr.startswith('hello'))
print(mystr.startswith('hel')) # True
print(mystr.startswith('hels')) # False

# 2.endswith
print(mystr.endswith('Python'))
print(mystr.endswith('python')) # 区分大小写

'''
判断拓展
函数：
    1.isalpha() -- 如果字符串中所有字符都是字母返回 True，否则返回 False
    2.isdigit() -- 如果字符串中所有字符都是数字返回 True，否则返回 False
    3.isalnum() -- 如果字符串中所有字符都是字母或都是数字或字母和数字的组合，则返回 True，否则返回 False
    4.issapace() -- 如果字符串中所有字符都是空白返回 True，否则返回 False
'''

# 1.isalpha()
print(mystr.isalpha()) # 因为有空白字符，所以不全是字母，返回 False
mystr1 = 'hello'
print(mystr1.isalpha()) # True

# 2.isdigit()
print(mystr.isdigit()) # False
mystr2 = '12345'
print(mystr2.isdigit()) # True

# 3.isalnum()
print(mystr.isalnum()) # 因为有空白字符，则返回 False
mystr3 = 'abc123'
print(mystr3.isalnum()) # True

# 4.isspace()
print(mystr.isspace()) # False
