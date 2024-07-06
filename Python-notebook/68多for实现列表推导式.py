'''
多 for 循环实现的列表推导式

实质是推导式遇到了 for 循环嵌套
'''

# 需求：创建如下列表
# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 1.方式1 -- 传统 for 循环嵌套实现
list1 = []
for i in range(1, 3, 1):
    for j in range(0, 3, 1):
        list1.append((i, j))

print(list1)

# 方式2 -- 多 for 列表推导式
list2 = [(l, m) for l in range(1, 3, 1) for m in range(0, 3, 1)]

print(list2)



