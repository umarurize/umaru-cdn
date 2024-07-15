'''
文件操作 -- 读取：
    1.read()
    语法 -- 文件对象.read(num)
    num 表示要从文件中读取数据的长度（单位是字节），如果没有传入 num，那么就是读取文件中所有的数据

    2.readlines()
    readline() 可以按照 '行' 的方式把整个文件中的内容进行一次性读取，并且返回一个列表，其中每一行的数据为一个元素

    3.readline()
    readline() 一次性只读取一行内容
'''

# 1.read()
f = open('test3.txt', 'r')
# print(f.read())  返回了所有的数据
# print(f.read(10)) 返回了9个数据，因为文件中数据换行了，所以 /n 占了一个字节


# 2.readlines()
# content = f.readlines() 返回 ['aaaaa\n', 'bbbbb\n', 'ccccc\n', 'ddddd\n', 'eeeee']，/n 也随之输出；但最后一个数据后面没有跟着 /n，因为最后一行并没有换行
# print(content)


# 3.readline()
content1 = f.readline()
print(f'第一行：{content1}') # 返回 aaaaa（第一行数据）

content1 = f.readline()
print(f'第二行：{content1}') # 返回 bbbbb（第二行数据）

f.close()




