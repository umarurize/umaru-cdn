'''
修改数据
    1.修改指定下标数据
    2.逆置：reverse()
    3.排序：sort() 升序和降序
'''

# 1.修改指定下标的数据
name_list =['Tom', 'Lily', 'Rose']
name_list[0] = 'aaa' # 直接 = 赋值即可
print(name_list)

# 2.逆序 reverse()
list1 = [1, 3, 6, 4, 5, 2]
list1.reverse()
print(list1)

# 3.sort()
# sort() 默认是升序排序，默认 reverse = False；升序则需要设置 reverse = True
list1.sort(reverse = True) # 升序则设置 reverse = False
print(list1)
