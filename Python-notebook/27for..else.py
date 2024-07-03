'''
for..else
'''
str1 = 'itheima'
for i in str1:
    print(i)
else:
    print('输出完毕') # for 正常结束执行的代码

'''
for..else 配合 break
'''
str2 = 'iloveu'
for j in str2:
    if j == 'o':
        break
    print(j)
else:
    print('输出完毕') # 当 for 被 break 打断，else 不执行

'''
for..else 配合 continue
'''
str3 = 'python'
for k in str3:
    if k == 'y':
        print('不输出y')
        continue
    print(k)
else:
    print('输出完毕')