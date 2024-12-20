'''
函数的参数（共包含4种写法）：
    1.位置参数
    2.关键字参数
    3.缺省参数
    4.不定长参数
'''


# 1.位置参数 -- 注意传递和定义参数的顺序和个数必须一致
def user_info(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info('Tom', 20, '男')
# user_info('Tom', 20) -- 报错，个数不一致
user_info(20, 'Tom', '男') # 返回 '您的名字是20, 年龄是Tom, 性别是男'，这样的数据是没有意义的


# 2.关键字参数
'''
在上一个例子中看出，传递参数和定义参数虽然顺序不一致，但也不会报错，需要避免这个问题。

在函数调用中，通过 '键=值' 形式加以指定，可以让函数更加清晰，容易使用，这样也同时理清了参数的顺序需求
'''


def user_info1(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info1('Rose', age = 20, gender = '女') # 返回 您的名字是Rose, 年龄是20, 性别是女
user_info1('小明', gender = '男', age = 16) # 返回 您的名字是小明, 年龄是16, 性别是男 -- 关键字参数之间不区分先后顺序

# user_info1(age = 20, gender = '男', 'Tom') -- 报错，因为位置参数必须写在关键字参数前面


# 3.缺省参数
'''
缺省参数即默认参数，用于定义函数时，为参数提供默认值

调用函数时，不可传递该默认参数的值

所有的位置参数必须出现在默认参数之前，包括定义和调用
'''


def user_info2(name, age, gender = '男'): # 设置默认参数（缺省参数）为 '男'
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


user_info2('Tom', 20) # 返回 '您的名字是Tom, 年龄是20, 性别是男'，因为 gender 为缺省参数
user_info2('Rose', 18, '女') # 返回 '您的名字是Rose, 年龄是18, 性别是女'


# 4.不定长参数（见83）

