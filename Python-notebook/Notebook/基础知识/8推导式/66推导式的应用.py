# 1.需求：创建一个0-10的列表

# 方式1 -- while 循环实现
list1 = [] # 准备1个空列表

i = 0
while i <= 10:
    list1.append(i)
    i += 1
print(list1)

# 方式2 -- for 循环实现
list2 = []

for i in range(0, 11, 1):
     list2.append(i)

print(list2)

# 方式3 -- 列表推导式实现

list3 = [i for i in range(0, 11, 1)] # 列表推导式中读与写都从 for 开始
print(list3)

