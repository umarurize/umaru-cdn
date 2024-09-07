'''
enumerate()
    函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，
    同时列出数据和数据下标，一般用在 for 循环当中
语法：
    enumerate(可遍历对象, start = 0) -- start 参数用来设置遍历数据的下标的起始值，默认为0
'''

list1 = ['a', 'b', 'c', 'd', 'e']

for i in enumerate(list1):
    print(i) # 返回元组，元组第一个数据是原迭代对象的下标，第二个数据是原迭代对象的数据 -- 并且默认 start = 0

for k in enumerate(list1, start = 1):
    print(k)





