age = 18
name = 'Tom'
weight = 75.5
student_id = 12

print('今年我的年龄是%d岁' % age)
print('我的名字是%s' % name)
print('我的体重是%.2f公斤' % weight)
print('我的学号是%03d' % student_id)

#我的名字是x，年龄是x岁
print('我的名字是%s,今年我的年龄是%d岁' % (name, age))

#我的名字是x，我明年x岁（直接做加法运算）
print('我的名字是%s,明年我的年龄是%d岁' % (name, age + 1))

#我的名字是x，今年年龄是x岁，体重x公斤，学号是x
print('我的名字是%s,今年年龄是%d岁, 体重%.2f公斤, 学号是%03d' % (name, age, weight, student_id))