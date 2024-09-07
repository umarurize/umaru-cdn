# 需求：任意两个数字，按照指定要求整理（求绝对值或求四舍五入）数字后再进行求和计算

# 1.求绝对值计算后再求和
# 1.1 方法1
def add_num(a, b):
    return abs(a) + abs(b)


result = add_num(-1, 2)
print(result) # 返回 3


# 1.2 方法2
def sum_num(a, b, f, e):
    return f(a) + e(b)


result1 = sum_num(-1, 1.9, abs, round) # 这里高阶函数 abs 和 round 直接作为实参传入
print(result1) # 返回 3

# 不难发现高阶函数的好处就是一次性完成多种数据处理，而不用重新定义新的函数