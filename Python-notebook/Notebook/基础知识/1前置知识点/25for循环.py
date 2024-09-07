'''
for 临时变量 in 序列:
    重复执行代码1
    重复执行代码2
    ....
其中：临时变量是自定义的，序列一般是数据
'''

str1 = 'itheima'

for i in str1:
    print(i) # 将这些数据逐个输出

'''
break 退出 for 循环
'''
str2 = 'Python'
for j in str2:
    if j == 'y':
        print('不输出 y') # 执行到条件成立，整个循环终止
        break
    print(j)

'''
continue 配合 for 循环
'''
str3 = 'iloveu'
for k in str3:
    if k == 'o':
        print('不输出 o')
        continue # 这里不需要和 while 循环一样，改变计数器的值
    print(k)
