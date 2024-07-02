''''
1.打印1个*
2.一行打5个，并显示在1行
3.上一步的打印5行
'''
j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*', end='')
        i += 1
    print() # 输出完1行，再换1行
    j += 1

print()

'''
打印*号（三角形）
每行*输出的个数和行号是相等的
'''
a = 0
while a < 5:
    b = 0
    while b <= a:
        print('*', end='')
        b += 1
    print()
    a += 1


