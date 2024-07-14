'''
测试引用是否能作为实参传递
'''


def test1(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))


b = 100
test1(b) # 返回的内存地址不同，因为 int 是不可变类型

c = [11, 22]
test1(c) # 返回的内存地址相同，因为 list 是可变类型

'''
小结：
    无论是可变类型还是不可变类型，都能够作为实参传入
'''
