'''
while 语法格式
while 条件
    条件成立重复执行的代码1
    条件成立重复执行的代码2
    ....
'''

# 需求：重复输出五次 wife i was wrong
# 因此需要一个数据来存储循环的次数

i = 0
while i < 5:
    print('wife, i was wrong')
    i += 1 # i=i+1

print('mission complete!')

'''
计数器的书写习惯：
计数器的第一个数一般取 0 ，而不是取 1
'''

# 循环应用：1-100累加
a = 1
result = 0

while a <= 100:
    result += a
    a += 1

print(f'结果是{result}')

# 循环应用：1-100内的偶数做累加
# 方式1
b = 1
result1 = 0

while b <= 100:
    if b % 2 == 0:
        result1 += b
    b += 1

print(f'100以内的偶数累加和是{result1}')

# 方式2
result2 = 0
c = 0
while c <= 100:
    result2 += c
    c += 2

print(f'100以内的偶数累加和是{result2}')

'''
书写 while 语句时的注意事··
'''


