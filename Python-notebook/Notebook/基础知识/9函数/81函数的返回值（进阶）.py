'''
思考：如果一个函数有两个返回值，那么程序会如何执行？
'''


def return_num():
    return 1
    return 2


result = return_num()
print(result) # 返回 1，因为 return 有退出函数的功能，所以 return 下方的函数不执行

"""
一个函数有多个返回值，该如何书写代码？
"""


def return_num1():
    return 1, 2


result1 = return_num1()
print(result1) # 返回一个元组 (1, 2)

'''
关于 return a, b 写法的注意事项：
    1.在返回多个数据时，默认是元组类型
    2.return 后面还可以连接列表、元组或字典，用来返回多个数据  
'''


# return 后面直接加元组
def return_num2():
    return (10, 20)


result2 = return_num2()
print(result2) # 返回 (10, 20) -- 元组类型


# return 后面直接加列表
def return_num3():
    return [10, 20]


list1 = return_num3()
print(list1) # 返回 [10, 20] -- 列表类型

# return 后面直接加字典也是同理



