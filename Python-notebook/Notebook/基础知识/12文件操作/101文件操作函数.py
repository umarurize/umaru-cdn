'''
文件和文件夹的操作：
    在 Python 中文件和文件夹的操作要借助 os 模块里相关功能；相关功能分为文件和文件夹两大类

    操作方法：
        1.导入 os 模块 -- import os
        2.使用 os 模块中的相关功能 -- os.函数名()
'''

import os


'''
文件操作函数：
    1.文件（文件夹）重命名 -- os.rename(目标文件名, 新文件名)
    2.删除文件 -- os.remove(目标文件名)
'''
# 1.文件重命名
os.rename('test.txt', 'test-rename.txt')

# 2.文件删除
os.remove('test1.txt')





