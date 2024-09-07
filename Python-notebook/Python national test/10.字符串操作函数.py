'''
1.字符串常用方法
    方法                      描述
    .lower()                  返回字符串的副本，全部字符小写
    .upper()                  返回字符串的副本，全部字符大写
    .split(sep=None)          返回一个列表，由字符串根据 sep 被侵害的部分构成，省略 sep 则默认以空格分隔
    .count(sub)               返回子串 sub 出现的次数
    .replace(old, new)        返回字符串的副本，所有 old 子串被替换为 new 子串
    .center(width, fill_char)  字符串居中函数，fill_char 参数可自定义
    .strip()                  从字符串中去掉其在左侧或右侧的自定义字符
    str.join(iter)            将 iter 遍历后，在 iter 的每一个元素后（不包含最后一个元素）插入 str
'''

# 1.1 .lower() and .upper()
str1 = 'HOW ARE YOU?'
str2 = 'how are u?'
print(str1.lower()) # return how are you?
print(str2.upper()) # return HOW ARE U?

# 1.2 .split(sep = None)
mystr = 'asd-f-ew-we-d-23-sf'
print(mystr.split('-')) # return ['asd', 'f', 'ew', 'we', 'd', '23', 'sf']

# 1.3 .count(sub)
mystr1 = 'abc234we32abcefabcabc'
print(mystr1.count('abc')) # return 4，因为子串 'abc' 在字符串中出现了 4 次

# 1.4 .replace()
print(str1.replace('O', '哈哈')) # return H哈哈W ARE Y哈哈U?

# 1.5 .center(width, fill_char)
str3 = 'hello'
print(str3.center(11, '-')) # return ---hello---
print(str3.center(11)) # 如果不填写 fill_char，则填充空格
print(str3.center(2)) # return hello 本身 -- 即当 width 小于 字符串本身长度，则返回字符串本身

# 1.6 .strip()
str4 = '   Python   '
print(str4.strip()) # return Python -- 即如果.strip() 中不填写参数，则默认去除空格

# 1.7 .join(iter)
print(','.join('Python')) # return P,y,t,h,o,n

mylist = ['你好', 'a', 'hello']
print(','.join(mylist)) # return 你好,a,hello


'''
2.字符串常用操作函数
    函数      描述
    len(x)    返回字符串 x 的长度，也可以返回其它组合数据类型的元素个数
    str(x)    返回任意类型 x 所对应的字符串形式
    chr(x)    返回 Unicode 编码 x 对应的单个字符
    ord(x)    返回单字符 x 表示的 Unicode 编码
    hex(x)    返回整数 x 对应十六进制的小写形式字符串
    oct(x)    返回整数 x 对应八进制数的小写形式字符串            
'''

# 2.1 len()
second_str1 = 'hello'
print(len(second_str1)) # return 5，即 second_str1 字符串的长度
second_list1 = ['hello', 5, [1, 2]]
print(len(second_list1)) # return 3，即 len() 也适用于组合数据类型

# 2.2 str()
second_a = 123
print(type(str(second_a))) # return <class 'str'>，实现了 str 数据类型转换

# 2.3 chr()
# Unicode 编码解释 -- 计算机认识的最底层的机器语言实质上是不同的 0 和 1 的组合，任何一种输入法都有他的编码格式（例如 gbk, iso, Python 底层的编码格式为 Unicode 编码）
print(chr(97)) # return a，即十进制数 97 被转换为 Unicode 二进制数 a

# 2.4 ord() -- 与 chr() 正好相反
print(ord('a')) # return 97

# 2.5 hex() and oct()
print(hex(20)) # return 0x14
print(oct(20)) # return 0o24


'''
3.字符串常用操作函数-拓展
    函数                      描述
    capitalize()              将字符串首字母转为大写，又称标题字符串  
    index(sub, begin, end)    返回子串 sub 在当前字符串中第一次出现的位置，并返回位置下标；如果没有找到，则报错  
    find(sub, begin, end)     返回子串 sub 在当前字符串中第一次出现的位置，并返回位置下标；如果没有找到，则返回 -1
'''

# 3.1 capitalize()
third_str1 = 'hello world and Python'
print(third_str1.capitalize()) # return 'Hello world and python‘
