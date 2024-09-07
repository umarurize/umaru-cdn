'''
拆包：
    1.元组拆包
    2.字典拆包
'''


def return_num():
    return 100, 200


result = return_num()
print(result) # 返回 (100, 200)，得到一个 tuple 型

num1, num2 = return_num() # tuple 拆包，用两个变量去接收数据
print(num1) # 返回 100
print(num2) # 返回 200


# 2.字典拆包
dict1 = {'name': 'Tom', 'age': 18}

a, b = dict1 # 对字典进行拆包，拿到的是 key 值。有了 key 值，就可以寻找相应的 value 值

print(a) # 返回 name
print(b) # 返回 age

print(dict1[a]) # 返回 Tom
print(dict1[b]) # 返回 18
