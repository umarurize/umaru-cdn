import re

# findall(正则表达式, 字符串) -- 匹配字符串中所有符合正则的内容
list = re.findall(r'\d+', '我的电话是：10086，我女朋友的电话是：10010')
print(list) # return ['10086', '10010']
for i in list:
    print(i)

# finditer(正则表达式, 字符串) -- 匹配字符串中所有的内容，返回一个迭代器
it = re.finditer(r'\d+', '我的电话是：10086，我女朋友的电话是：10010')
print(it) # return <callable_iterator object at 0x000002780C319128>
for i in it:
    print(i.group()) # 想要拿到迭代器中的内容，需要借助 .group() return 10086 10010

# search() -- 找到一个匹配结果就返回
str = re.search(r'\d+', '我的电话是：10086，我女朋友的电话是：10010')
print(str.group()) # return 10086，并没有返回 10010

# match() match 从第一个字符开始匹配，匹配不到则报错
# str1 = re.search(r'\d+', '我的电话是：10086，我女朋友的电话是：10010')
str1 = re.match(r'\d+', '0086，我女朋友的电话是：10010') # return 10086

# 预加载正则表达式 -- 可以反复使用，简化代码
obj = re.compile(r'\d+')
it1 = obj.finditer('我的电话是：10086，我女朋友的电话是：10010')
for i in it1:
    print(i.group()) # return 10086， 10010


# 案例
str2 = '''
<div class='jay'><span id='1'>周杰伦</span></div>
<div class='jj'><span id='2'>林俊杰</span></div>
<div class='jay'><span id='3'>大聪明</span></div>
<div class='jay'><span id='4'>范思哲</span></div>
'''

# 预加载正则表达式
# 二次筛选正则匹配 (?P<自定义名字>正则表达式 )
obj1 = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<chinese_name>.*?)</span></div>", re.S) # re.S 让 . 能匹配换行符

result = obj1.finditer(str2)
for i in result:
    print(i.group('id'))
    print(i.group('chinese_name'))

