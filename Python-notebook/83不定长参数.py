'''
不定长参数
定义：
    不定长参数又称可变参数，用于不确定调用时会传递多少个参数（不传递也可以）的场景。

    这时候，进行参数传递的方式有两种
        1.包裹 (packing) 位置参数
        2.包裹关键字参数
'''


# 1.包裹位置参数传递
def user_info(*args): # *args 用于接收不定长参数
    print(args)


user_info('Tom') # 返回 ('Tom',)
user_info('Tom', 18) # 返回 ('Tom', 18)
user_info('Tom', 18, 'man') # 返回 ('Tom', 18, 'man')
user_info() # 返回 ()，一个空的元组

'''
小结：
    传进去的所有参数都会被 args 变量收集，它会根据传进参数的位置合并为一个元组（tuple）
    
    args 是元组类型
'''


# 2.包裹关键字参数传递
def user_info1(**kwargs):
    print(kwargs)


user_info1() # 返回 {}，一个空字典
user_info1(name = 'Tom') # 返回 {'name': 'Tom'}
user_info1(name = 'Tom', age = 20) # 返回 {'name': 'Tom', 'age': 20}

'''
小结：
    ...... 用法和 *args 相同，只不过返回的是字典
    
'''

'''
总结：
    无论是包裹位置传递，还是包裹关键字传递，都是一个组包的过程
'''