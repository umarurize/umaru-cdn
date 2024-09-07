'''
for 循环在列表和元组中的应用
    - 应用场景 -- 可迭代对象：如字符串、列表、元组、字典等可以用来循环遍历的数据
    - 语法：
            for <循环变量> in <可迭代对象>:
                <循环体>
    - 注：二级考试中，while 称作无限循环；for 称作遍历循环
'''
list1 = [1, 2, 3, 'hello', [1, 2]]
for i in  list1:
    print(i, end = '==') # 依次输出可迭代对象中的每一个元素

# for 循环在 tuple 中的应用也是同理