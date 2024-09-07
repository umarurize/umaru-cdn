'''
文件夹操作函数：
    1.创建文件夹 -- os.mkdir(文件夹名字)
    2.删除文件夹 -- os.rmdir(文件夹名字)
    3.获取当前目录 -- os.getcwd()
    4.改变默认目录 -- os.chdir(目录)
    5.获取目录列表 -- os.listdir(目录)
    6.重命名文件夹
'''

import os

# 1.创建文件夹
# os.mkdir('mkdir-test')

# 2.删除文件夹
# os.rmdir('mkdir-test')

# 3.获取当前目录
print(os.getcwd()) # 返回当前文件所在目录

'''
# 4.改变默认目录
# 需求：在 aa 文件夹中创建 bb 文件夹
# step1 -- 切换目录到 aa
# step2 -- 创建目录 bb
# os.chdir('aa')
# os.mkdir('bb')
'''

# 5.调用目录列表
print(os.listdir()) # 返回一个列表，列表里的元素是文件下的所有文件
print(os.listdir('aa'))

# 6.重命名文件夹
os.chdir('aa')
os.rename('bb', 'bb-rename')


