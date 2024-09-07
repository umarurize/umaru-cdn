'''
函数嵌套调用模拟：
'''


# 两个函数 testA 和 testB -- 并在 A 里面嵌套调用 B
# 定义函数B
def testB():
    print('B函数开始---')
    print('B函数结束---')


# 定义函数A
def testA():
    print('A函数开始---')
    testB()
    print('A函数结束---')


# 调用函数
testA()  # 嵌套调用成功

'''
函数嵌套调用实例：
'''


# 案例1 -- 打印一条横线
def print_line():
    print('-' * 20)


print_line()  # 返回 --------------------


# 案例2 -- 打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(5)  # 打印了5条横线


# 案例3 -- 函数嵌套计算
def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)
print(result) # 返回 6


# 案例4 -- 求三个数的平均值
def average_num(a, b, c):
    sumResult = sum_num(a, b, c)
    return sumResult / 3


result1 = average_num(1, 2, 3)
print(result1) # 返回 2.0 （注意除法输出的都是 float 型）
