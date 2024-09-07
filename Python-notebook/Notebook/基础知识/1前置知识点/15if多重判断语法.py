'''
需求：
中国合法工作年龄为18-60岁，即如果年龄小于18的情况视为童工，不合法；
年龄再18-60岁为合法工龄；
大于60岁为法定退休年龄

因此这里就有了三种情况
'''

age = int(input('请输入您的年龄:'))

if age < 18:
    print(f'您的年龄是{age}岁，是违法的')
elif age > 60:
    print(f'您的年龄是{age}岁，该退休了')
else:
    print(f'您的年龄是{age}岁，符合合法工作年龄')

print('系统关闭')

# 方式2
age1 = int(input('请输入您的年龄：'))

if age1 < 18:
    print(f'您的年龄是{age1}岁，是违法的')
elif (age1 >= 18) and (age1 <= 60):
    print(f'您的年龄是{age1}岁，符合合法工作年龄')
else:
    print(f'您的年龄是{age1}岁，该退1休了')

print('系统关闭')

# 方式3 针对复杂条件的代码化简
age2 = int(input('请输入您的年龄：'))
if age2 < 18:
    print(f'您的年龄是{age2}岁，是违法的')
elif 18 <= age2 <= 60:
    print(f'您的年龄是{age2}岁，符合合法工作年龄')
else:
    print(f'您的年龄是{age2}岁，该退休了')

print('系统关闭')
