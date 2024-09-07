'''
函数
    1. 函数的作用：
        - 降低编程难度
        -增加代码复用
    2. 语法：
        def 函数名(形参列表)
            函数体
            return 返回值 （可有可无）
'''


def add_sum(a):
    result = 0
    i = 1
    while i <= a:
        result += i
        i += 1
    return result


print(add_sum(100)) # return 5050 -- 相当于 1-100 的累加


'''
函数的返回值
'''


def exchange_num(a, b):
    return b, a # 交换位置


m, n = exchange_num(1, 2)
print(m) # return 2
print(n) # return 1


'''
函数的参数 -- 缺省参数
'''


def add_num(a, b = 5):
    return a + b


result = add_num(10)
print(result) # return 15, 因为 b = 5 是缺省参数


'''
函数变量的作用域（局部变量和全局变量）
    1. 局部变量 -- 在函数内部定义的变量，仅在函数内部有效，当函数退出时，变量将不再存在
    2. 全局变量 -- 全局变量在函数内部使用时，需要提前使用保留字 global 声明
        语法 -- global <全局变量>
'''


def info_print():
    a = 1
    b = 2
    print(a, b)

info_print() # return 1 2

# print(a, b) -- 报错，因为 a, b 是定义在函数内部的局部变量，在函数外部则是未定义的

k = 2
def func(a, b):
    global k
    k = a * b
    print(k)


func(5, 6) # return 30
print(k) # return 30


