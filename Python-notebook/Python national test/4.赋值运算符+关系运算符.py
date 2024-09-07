'''
1. 运算符-赋值运算符
    运算符     举例      描述
    =         x = 1     将 1 赋值给变量 x
    +=        x += 1    x = x + 1
    -=        x -= 1    x = x - 1
    *=        x *= 1    x = x * 1
    /=        x /= 1    x = x / 1
    //=       x //= 1   x = x // 1 （取整）
    %=        x %= 1    x = x % 1 （取余）
    **=       x **= 1   x = x ** 1
'''
a = 1
b = 2
a, b = b, a # 相当于把 a 和 b 的赋值调换
print(f'{a} and {b}') # return 2 and 1
print('a 的值是' + str(a)) # return a 的值是2


'''
2.1 运算符-关系运算符
    运算符     举例      描述
    <         x < y     判断 x 是否小于 y
    >         x > y     判断 x 是否大于 y
    <=
    >=
    ==        x == y    判断 x 是否等于 y
    !=        x != y    判断 x 是否不等于 y
计算后的结果值类型为 bool 型       

2.2 运算符-逻辑运算符
    运算符     举例      描述
    not       not x     如果 x 值为 True, 结果为 False; 如果 x 值为 False, 结果为 True
    and       x and y   x 或 y 任一个为 False, 结果为 False; 都为 True 则结果为 True
    or        x or y    x 或 y 任一个为 True, 结果为 True; 都为 False 则结果为 False        
'''

