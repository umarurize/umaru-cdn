# 1.float() 函数
num1 = 1
str1 = '10'
print(type(float(num1))) # float
print(float(num1)) # 1.0
print(float(str1)) # 10.0

# 2. str()
print(type(str(num1))) # str

# 3. tuple() 将一个序列转换为元组
list1 = [10, 20, 30]
print(tuple(list1))

# 4. list() 将一个元组转换为列表
t1 = (100, 200, 300)
print(list(t1))

# 5. eval() 计算字符串中的有效Python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000, 3000)'
str5 = '[1000, 2000, 3000]'
print(type(eval(str2)))
