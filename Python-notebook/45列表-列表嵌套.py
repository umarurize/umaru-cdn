'''
列表嵌套指的是一个列表里面包含了其它的子列表
'''

# 1.需求：要存储班级一、二、三三个班级学生姓名，且每个班级的学生姓名在一个列表
name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]

print(name_list)

print(name_list[0])

print(name_list[0][2])
