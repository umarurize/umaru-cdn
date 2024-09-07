'''
1.列表索引
    - 索引用来表示列表中元素的位置
    - 基于位置，可以快速找到其对应的列表元素
    - 如果一个列表中有 n 个元素，那么索引的取值范围为 0~n-1
'''
first_list1 = [1, 'hello', [1, 2]]
print(first_list1[2]) # return [1, 2]
print(first_list1[2][0]) # return 1

print(first_list1[::-1]) # return [[1, 2], 'hello', 1] -- 即将列表中的元素逆序排列


'''
2.列表的常用操作函数
    函数或方法           描述
    x in t              x 在 t 中，返回 True；不在则返回 False
    x not in t          x 在 t 中，返回 False；不在则返回 True
    len(x)              返回列表 x 中元素的个数
    min(x)              返回列表 x 中的最小元素
    max(x)              返回列表 x 中的最大元素
    
    注：对于存放字符串的列表，在用 min() 和 max() 时，比较的是字母的顺序大小
'''


'''
3.列表的常用操作方法
    方法              描述
    .append(x)        在列表末尾处追加一个新元素 x
    .insert(i, x)     在列表第 i 位增加元素 x
    .clear()          清空列表
    .pop(i)           将列表中第 i 个元素删除
    .remove(x)        将列表中出现的第一个元素 x 删除
    .reverse()        将列表中的元素反转
    .index(x)         返回列表中第一次出现元素 x 的位置下标
    .count(x)         返回列表中出现 x 的次数
    .copy()           返回一个新列表，复制列表中的元素                    
'''
third_list1 = [123, 'hello', [1, 2]]

# 3.1 .insert(i, x)
third_list1.insert(2, 'world')
print(third_list1) # return [123, 'hello', 'world', [1, 2]]

# 3.2 .pop(i)
third_list1.pop()
print(third_list1) # return [123, 'hello', 'world'] -- 即 .pop() 不填入参数时，默认删除最后一个元素

# 3.3 .index()
index0 = third_list1.index('hello')
print(index0) # return 1 -- 即 'hello' 在列表中所处的位置下标
third_list1.pop(index0)
print(third_list1) # return [123, 'world'] -- 综合使用 .index() 和 .pop()

# 3.4 .copy()
third_list2 = third_list1.copy()
print(third_list2) # return [123, 'world'] -- 注意这里 third_list2 在内存中开辟了新的空间






