'''
lambda应用：
    1.带判断的 lambda
    2.列表数据按字典 key 值排序
'''


# 1.带判断的 lambda
fn1 = lambda a, b: a if a > b else b # 因为 lambda 函数只能返回一结果，因此三目运算符在这里是适用的
print(fn1(1000, 500)) # 返回 1000


# 2.列表数据按字典 key 值排序
students = [{'name': 'Tom', 'age': 20},
            {'name': 'Rose', 'age': 19},
            {'name': 'Jack', 'age': 22}]

# 需求1：按name值升序排列
students.sort(key = lambda x: x['name'])
print(students)

# 需求1：按name值降序排列
students.sort(key = lambda x: x['name'], reverse = True)
print(students)