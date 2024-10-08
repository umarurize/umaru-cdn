'''
集合之增加数据：
    1.add() -- 增加单一数据
    2.update() -- 增加序列数据
'''

# 1.add()
s1 = {10, 20}
s1.add(100)
print(s1) # 输出 {100, 10, 20} -- 说明集合是可变类型，add() 追加数据时，可以追加到任意位置，因为集合里的数据没有顺序之分

s1.add(100)
print(s1) # 输出 {100, 10, 20} -- 没有追加第二个 100，因为集合有去重功能

# s1.add([10, 20, 30]) -- 报错，说明 add() 只能增加单一数据

# 2.update()
s2 = {10, 20}
s2.update([10, 20, 30, 40, 50])
print(s2) # 输出 {40, 10, 50, 20, 30}
# s2.update(100) -- 报错，因为 update() 只能追加序列，不能追加单一数据

'''
集合之删除数据：
    1.remove() -- 删除集合中的指定数据，如果数据不存在，则报错
    2.discard() -- 删除集合中的指定数据，如果数据不存在也不会报错
    3.pop() -- 随机删除集合中某个数据，并返回这个数据
'''

# 1.remove()
s3 = {10, 20, 30, 40, 50}
s3.remove(10)
print(s3) # 输出 {40, 50, 20, 30} -- 数据10被删除

# s3.remove(10) 报错 -- 因为数据10已经不存在了

# 2.discard()
s4 = {10, 20, 30, 40, 50}
s4.discard(10)
print(s4) # 输出 {40, 50, 20, 30} -- 数据10被删除，这点功能和 remove() 一样

s4.discard(10)
print(s4) # 不报错 -- 即便数据不存在，discard() 也不会报错

# 3.pop()
s5 = {10, 20, 30, 40, 50}
del_num = s5.pop()
print(del_num) # 输出 40，数据40被随机删除了
print(s5) # 输出 {10, 50, 20, 30}



