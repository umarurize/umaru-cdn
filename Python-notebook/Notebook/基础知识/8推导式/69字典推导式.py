'''
字典推导式：
    思考：如果有如下两个列表
    list1 = ['name', 'age', 'gender']
    list2 = ['Tom', 20, 'man']
    如何快速合并为1个字典

    这里就需要用到字典推导式

字典推导式的作用：
    快速合并列表为字典或提取字典中的目标数据
'''

# 实例1 -- 需求：创建1个字典，key 是数字1-5，value 是对应数字的 2 次方
dict1 = {i: i ** 2 for i in range(1, 6, 1)}
print(dict1) # 返回 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 实例2 -- 合并两个列表为字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']

dict2 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict2) # 返回 {'name': 'Tom', 'age': 20, 'gender': 'man'}

'''
字典推导式作用拓展：
    提取字典中的目标数据
'''

# 需求：提取下面电脑售出数量大于等于200的字典数据
counts = {'MAC': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1) # 返回 {'MAC': 268, 'DELL': 201}
