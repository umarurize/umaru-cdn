name = 'Tom'
age = 18
weight = 75.5

# 我的名字是x，今年x岁了，体重x公斤
print('我的名字是%s，今年%d岁了，体重%.2f公斤' % (name, age, weight))
# 方式2，%s 整型、浮点型、字符都能格式化输出
print('我的名字是%s，今年%s岁了，体重%s公斤' % (name, age, weight))

