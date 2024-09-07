'''
元组
    1. 元组和列表同属于序列，但两者本质上的不同在于，元组是不可修改的数据
    2. 元组用 () 表示
    3.元组的常用操作方法和函数
        函数或方法           描述
        x in t              如果 x 在 t 中，返回 True；不在则返回 False
        x not in t          如果 x 在 t 中，返回 False；不在则返回 True
        len(t)              .....
        min(t)              .....
        max(t)              .....
        .index(x)           返回元组中第一次出现元素 x 的位置
        .count(x)           返回元组中出现元素 x 的次数
'''
tuple1 = (123, 23, 'hello', [1, 2])

# 1.选区输出
print(tuple1[0:2]) # return (123, 23)


# 2.如果元组中只有一个元素
tuple2 = (1,)
print(type(tuple2)) # return <class 'tuple'> -- 即元组中只有一个元素时，必须在末尾加逗号

tuple3 = (1)
print(type(tuple3)) # return <class 'int'> -- 错误示范