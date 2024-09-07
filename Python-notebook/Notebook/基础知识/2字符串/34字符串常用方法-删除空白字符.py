'''
字符串删除首位空白的函数
    1.lstrip() --- 删除字符串左侧的空白字符
    2.rstrip() --- 删除字符串右侧的空白字符
    3.strip() --- 删除字符串两侧的空白字符
'''

# 1.lstrip()
mystr = '   hello world and itcast and itheima and Python   '

print(mystr)

new_str = mystr.lstrip()
print(new_str) # 删除左侧空白

# 2.rstrip()
new_str1 = mystr.rstrip()
print(new_str1) # 删除右侧空白

# 3.strip()
new_str2 = mystr.strip()
print(new_str2) # 删除两侧空白
