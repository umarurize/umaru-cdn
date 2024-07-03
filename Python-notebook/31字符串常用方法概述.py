'''
字符串常用的操作方法
主要分为三大类：查找、修改、判断
学习路线：
    1.记住函数名
    2.记住函数的作用
    3.记住函数的参数传递方式
'''

'''
1.查找
    即查找子串在字符串种出现的位置（查找下标）或出现的次数
2.函数
    .find(子串, 开始位置下标， 结束位置下标)
    .index(子串, 开始位置下标, 结束位置下标)
    .count(子串, 开始位置下标, 结束位置下标) --- 用于统计字符串出现的次数
'''

# 1.find() -- 检测某个子串是否包含在这个字符串当中，如果包含则返回该字符串开始位置的下标，否则返回-1
# 2.index() -- 功能与 find() 大致相同，不过不包含会报错

mystr = 'hello world and itcast and itheima and Python'

print(mystr.find('and')) # 返回 12 ，即 and 所在位置开始的位置下标

print(mystr.find('and', 15, 30))

print(mystr.find('ands')) # 不存在该子串，返回 -1

# print(mystr.index('ands'))

print(mystr.count('and', 15, 30))

print(mystr.count('and'))

print(mystr.count('ands')) # 不存在则返回 0

'''
拓展：
    rfind()、rindex()
    用法和 find()、index() 一样，不过是从右侧开始查找
'''
print(mystr.rfind('and')) # 结果还是从左边开始数，不过查找顺序是从右向左

# rindex() 同理