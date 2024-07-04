'''
capitalize()
作用：
    将字符串第一个字符转换成大写
    转换后，整个字符串第一个字符大写，其他字符全都小写
'''
mystr = 'hello world and itcast and itheima and Python'

new_str = mystr.capitalize()
print(new_str) # 可以看到 Python 的首字母变成了小写，hello 的首字母变成了大写

'''
title()
作用：
    字符串中每个单词首字母都大写
'''
new_str1 = mystr.title()
print(new_str1)

'''
upper()
作用：
    整个字符串都转换为大写
'''
new_str2 = mystr.upper()
print(new_str2)

'''
lower()
作用：
    整个字符串都转换为小写
'''
mystr1 = 'HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON'

new_str3 = mystr1.lower()
print(new_str3)

