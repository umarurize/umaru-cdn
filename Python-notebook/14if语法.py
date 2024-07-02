'''
if 条件:
    条件成立执行代码
只有条件成立才能输出
    ....
'''

if True:
    print('hello world')
    print('验证可执行多行代码')

# 下方没有缩进的代码不属于if代码块，与条件成立与否无关
print('hello Python')

if False:
    print('验证不成立是否可以输出')

# if应用实例：上网
# 需求：年龄大于等于18，输出：已经成年可以上网
# 准备年龄数据
age = 20

if age >= 18:
    print('已经成年，可以上网')

print('系统关闭')

# if应用实例：上网进阶版
age1 = int(input('请输入您的年龄:'))

if age1 >= 18:
    print(f'您的年龄是{age1}岁，已经成年，可以上网')

print('系统关闭')

# if..else应用实例：上网
age2 =int(input('请输入您的年龄:'))

if age2 >= 18:
    print(f'您的年龄是{age2}岁，已经成年，可以上网')
else:
    print(f'您的年龄是{age2}岁，小朋友回家写作业去')

print('系统关闭')

'''
if 语法注意事项
如果某些条件成立执行了相关的代码，那么其它解释器的代码不执行
'''
