'''
内置函数1
    函数名             描述
    abs(x)            返回 x 的绝对值，如果 x 是复数，则返回复数的模
    divmod(a, b)      返回 a 和 b 的商及余数。例如：divmod(10, 3) 返回的结果是 (3, 1)
    pow(x, y)         返回 x 的 y 此幂。例如：pow(2, pow(2, 2)) 返回的结果是 16
    round(n)          四舍五入方式计算 n
'''

# 1.1 abs(x)
print(abs(1 + 5j)) # return 5.0990195135927845 -- 即 (2^2 + 5 ^2) ** (0.5)

# 1.2 divmod(a, b)
print(divmod(10, 3)) # return (3, 1) -- 返回的是一个元组，元组中的数据分别对应商和余数

# ....


'''
内置函数2
    函数名              描述
    all(x)             组合类型变量 x 中所有元素都为真时返回 True；否则返回 False；当 x 为空时，也返回 True
    any(x)             组合类型变量 x 中任一元素为真时返回 True；否则返回 False；当 x 为空时，也返回 False
    reversed(x)        返回组合类型 x 的逆序形式
    sorted(x)          对组合数据类型 x 进行排序，默认从小到大
    sum(x)             对组合数据类型 x 计算求和结果   
'''

# 2.1 all(x)
list1 = [True, True, 1, 23, 'hello']
print(all(list1)) # return True -- 注：Python 中输入任何一个数据类型都会默认为 True，单数据 0 是特殊的，0 代表 False

list2 = [True, 1, 233, 'True', 0]
print(all(list2)) # return False

list3 = []
print(all(list3)) # return True

# 2.2 any(x)
print(any(list2)) # return True

list4 = [False, 0]
print(any(list4)) # return False

print(any(list3)) # return False

# 2.3 reversed(x)
list5 = ['hello', 123, [1, 2], True]
print(reversed(list5)) # return <list_reverseiterator object at 0x0000018589AF06D8> -- 返回了一个可迭代的对象
print(list(reversed(list5))) # return [True, [1, 2], 123, 'hello']
print(list5[::-1]) # return [True, [1, 2], 123, 'hello']

# 2.4 sorted()
list6 = [1, 23, 69, 27, 0]
print(sorted(list6)) # return [0, 1, 23, 27, 69] -- 默认从小到大

# 2.5 sum()
print(sum(list6)) # return 120 -- 将列表 list6 中的每个元素相加求和


'''
内置函数3
    函数名             描述
    eval(s)           计算字符串 s 作为 Python 表达式的值
    exec(s)           计算字符串 s 作为 Python 语句的值
    range(a, b, s)    从 a 到 b （不包含 b），以 s 为步长产生一个序列                       
'''

# 3.1 eval()
list7 = "['name', 123, 1, [4, 5]]"
print(eval(list7)) # return ['name', 123, 1, [4, 5]]
print(type(eval(list7))) # return <class 'list'>

# 3.2 exec()
exec('a = 1 + 99')
print(a) # return 100

# 3.3 range(a, b, s)
sum_result = 0
for i in range(1, 101, 1): # 或者 for i in range(4):
    sum_result += i
    print(sum_result) # return 5050




