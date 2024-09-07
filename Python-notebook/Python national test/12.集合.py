'''
集合-set
    1. Python 中集合类型和数学中的集合概念完全一致
    2. 集合用来存储无序且不重复的数据
    3. 集合中元素的类型只能是不可变数据类型，如：整数、浮点数、字符串、元组等
    4. 相比较而言，列表、字典、集合类型本身就是可变数据类型
'''
set1 = {123, 123, 3.14, 'abc', 'abc'}
print(set1) # return {3.14, 'abc', 123}


'''
集合类型的操作符
    操作符     描述
    s - t     返回一个新集合，包括在集合 s 中 但不在集合 t 中的元素
    s & t     返回一个新集合，包括同时在集合 s 和 t 中的元素
    s ^ t     返回一个新集合，包括集合 s 和 t 中的非同元素
    s | t     返回一个新集合，包括集合 s 和 t 中的所有元素        
'''
set2 = {123, 43, 12, 3424}
set3 = {123, 43, 12, 34545, 56567}

# 1. s - t 差集
print(set2 - set3) # return {3424}

# 2. s & t 交集
print(set2 & set3) # return {123, 43, 12}

# 3. s ^ t 补集
print(set2 ^ set3) # return {3424, 34545, 56567}

# 4. s | t 并集
print(set2 | set3) # return {3424, 43, 12, 34545, 56567, 123}


'''
集合常用的操作函数与方法
    函数或方法           描述
    s.add(x)             如果数据项 x 不在集合 s 中，将 x 添加到 s
    s.remove(x)          如果 x 在集合 s 中，移除该元素；不存在则报错 KeyError
    s.clear()            清空集合
    len(s)               返回集合 s 的元素个数
    x in s               存在返回 True；不存在返回 False
    x not in s           不存在返回 True；存在返回 False      
'''
set4 = {123, 345, 3.14, 5.25}

# 1. len()
print(len(set4)) # return 4

# 2.in and not in
print(123 in set4) # return True
print(123 not in set4) # return False

# ......

# 补充-创建空集合
set5 = set()
print(type(set5)) # return <class 'set'>

set6 = {} # 这样创建的是空字典

