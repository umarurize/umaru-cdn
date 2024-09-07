'''
range(strat, end, step) -- 生成从 start 到 end 的数字；step 为步长，可供 for 循环使用
'''

print(range(1, 10, 1)) # 不能拿到有效数字

for i in range(1, 10, 1):
    print(i)

for i in range(1, 10):
    print(i) # 效果同上，不写 step，则默认 step 为 1

for i in range(1, 10, 2):
    print(i) # 输出 1 3 5 7 9

for i in range(10):
    print(i) # 不写 start，则从 0 开始遍历

'''
range() 的注意事项
    1.如果不写 start，则从0开始
    2.如果不写 step，则默认 step 为1
    3.end 必须要写，否则会报错
'''