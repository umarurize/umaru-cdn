'''
seek()
    作用：用来移动文件指针
    语法：.seek(偏移量, 起始位置) -- 偏移量的单位为字节
    起始位置：
        0 -- 文件开头
        1 -- 当前位置
        2 -- 文件结尾
'''

'''
测试需求：
    1. r 访问模式下改变文件指针位置，改变读取数据开始位置，或把文件指针放结尾（即无法读取数据）
    2. a 访问模式，改变文件指针位置，从而可以读取出数据
'''

# 1.r 访问模式
f = open('test5.text', 'r+')

content = f.read()
print(content) # 读取出了所有数据，因为 r+ 访问模式的文件指针在开头

f.seek(2, 0)
content1 = f.read()
print(content1) # 第一行数据少读2个字节

f.seek(0 ,2)
content2 = f.read()
print(content2) # 读不出数据，因为文件指针被移动到了结尾

f.close()

print('')


# 2.a 访问模式
f1 = open('test6.txt', 'a+')

con = f1.read()
print(con) # 读不出数据，因为 a 访问模式的文件指针在末尾

f1.seek(0) # 参数是0，其实代表的是2个0，即不偏移且文件指针在开头
con1 = f1.read()
print(con1) # 读取出了所有数据，因为文件指针被移动到了开头

f1.close()







