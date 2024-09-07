''''
else 下方缩进的代指的是当循环正常结束之后要执行的代码
while 条件:
    条件成立重复执行的代码
else:
    循环正常结束之后执行的代码
'''

# 需求：女朋友生气了，要做如下惩罚
# 连续说5遍我错了，如果道歉完毕，获得了原谅，代码该怎么写？

i = 0
while i < 5:
    print('wife, i was wrong')
    i += 1
else:
    print('媳妇儿原谅我了..')

'''
while..else 配合 break
while..else 配合 continue
'''
# 需求：女朋友生气，要求道歉5遍。道歉到第3遍时，女朋友说这一遍不真诚，是否退出循环
# 可能性1：更生气，不打算原谅，不需要继续道歉了
# 可能性2：这一遍虽然不真诚，但可以忍受，继续下一步道歉即可

j = 0
while j < 5:
    if j == 3:
        print(f'第{j}遍道歉不真诚..不打算原谅')
        break
    print('wife, i was wrong')
    j += 1
else:
    print('女朋友原谅我了') # 如果 while 被 break 打断，那么 else 不执行

# 接着上面的可能性2

k = 0
while k <= 5:
    if k == 3:
        print(f'第{k}遍道歉不真诚，可以忍受，继续道歉')
        k += 1
        continue
    print('wife, i was wrong')
    k += 1
else:
    print(f'一共道歉{k-1}次，原谅你了..')