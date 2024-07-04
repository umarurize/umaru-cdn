'''
列表中删除数据
函数：
    1.del -- 语法：del 目标/del （目标）
    2.pop() -- 作用：删除指定下标的数据，如若不指定下标，则删除最后一个数据。pop() 会返回被删除的数据
    3.remove() -- 语法：remove(数据)
    4.clear() -- 作用：清空列表中所有的数据
'''

# 1.del
# -删除整个列表
name_list = ['Tom', 'Lily', 'Rose']
del name_list # del (name_list) 也可
# print(name_list) 报错，找不到 name_list

# -删除列表中某个数据
name_list1 = ['Tom', 'Lily', 'Rose']
del name_list1[0]
print(name_list1)

# 2.pop()
name_list2 = ['Tom', 'Lily', 'Rose']
del_name = name_list2.pop()
print(del_name)
del_name1 = name_list2.pop(1)
print(del_name1)

# 3.remove()
name_list3 = ['Tom', 'Lily', 'Rose']
name_list3.remove('Rose')
print(name_list3)

# 4. clear()
name_list4 = ['Tom', 'Lily', 'Rose']
name_list4.clear()
print(name_list4)