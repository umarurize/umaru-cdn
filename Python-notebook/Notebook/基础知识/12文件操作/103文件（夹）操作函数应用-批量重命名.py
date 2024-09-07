'''
批量重命名
    需求：批量修改文件名，既可添加指定字符串，又能删除指定字符串

    步骤：
        1.设置添加\删除字符串的标识
        2.获取指定目录的所有文件
        3.将原有文件名添加\删除指定字符串，构造新名字
        4.重命名
'''

import os

flag = 2

file_list = os.listdir()

for i in file_list:
    if flag == 1:
        new_name = 'Python_' + i
        os.rename(i, new_name)
    elif flag == 2:
        index = len('Python_') # index = 7
        new_name = i[index:] # 从下标7开始切片
        os.rename(i, new_name)