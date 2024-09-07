''''
字符串修改
函数（很多，只用记重点）
    1. .replace(旧字串, 新子串, 替换次数)
    2. .split(分割字串, 分割次数)
    3. .join()
'''

'''
replace 函数
替换的次数不写，那么将替换所有
'''

mystr = 'hello world and itcast and itheima and Python'

# 需求：用.replace() 将 and 换成 he
new_str = mystr.replace('and', 'he')
print(new_str)

new_str2 = mystr.replace('and', 'he', 1)
print(new_str2) # 如果替换次数大于字符串有的，那将全部替换

'''
split 函数
分割并返回一个列表
函数用法：
    字符串序列.split(分割字符, num)
    num指分割的次数，返回列表的数据是 num+1 个
'''

list1 = mystr.split('and')
print(list1) # 如果不写分割次数，那就全部分割，并丢失分割字符

list2 = mystr.split('and', 2)
print(list2) # list2 中返回了3个数据

'''
join 函数
合并列表里面的字符串数据为一个大字符串
'''

mylist = ['aa', 'bb', 'cc']

# 需求：将列表里的数据连接为 aa..bb..cc
new_str3 = '..'.join(mylist)
print(new_str3)






