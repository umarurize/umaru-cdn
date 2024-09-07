'''
while 循环嵌套应用
需求：有天女朋友生气了，惩发说3遍媳妇我错了
另外女朋友还说要刷今天的碗
这套惩罚重复3天该怎么执行？
'''

i = 1
while i <= 3:
    j = 1
    print('我刷今天的碗')
    i += 1
    while j <= 3:
        print('wife, i was wrong')
        j += 1
    print(f'第{i-1}天惩罚结束..')

print('所有惩罚结束..')


