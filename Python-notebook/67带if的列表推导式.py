''''
带 if 的列表推导式
'''

# 需求：创建 0-10 的偶数列表

# 方式1 -- 修改 range() 中的 step 参数
list1 = [i for i in range(0, 11, 2)]
print(list1) # 返回 [0, 2, 4, 6, 8, 10]

# 方式2 -- for 循环嵌套 if 实现
list2 = []
for i in range(11):
    if i % 2 == 0:
        list2.append(i)
print(list2) # 返回 [0, 2, 4, 6, 8, 10]

# 方式3 -- 带 if 的列表推导式实现
list3 = [i for i in range(11) if i % 2 == 0]
print(list3)