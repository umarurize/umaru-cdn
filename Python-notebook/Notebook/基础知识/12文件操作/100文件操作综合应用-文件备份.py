'''
综合应用 -- 文件备份

需求：
    用户输入当前目录下任意文件名，程序完成对该文件的备份功能（备份文件名为 xx[备份]后缀，例如：test[备份].txt）

步骤：
    1.接收用户输入的文件名
    2.规划备份文件名
    3.备份文件写入数据
'''


# 1.用户输入备份的目标文件名
old_name = input('请输入您要备份的文件名：')


'''
2.规划备份文件名
    2.1 提取后缀 -- 找到文件名中的.（最右侧的 . 才是后缀的 .） -- 文件名和后缀拆分
    2.2 组织新名字 = 原名字 + [备份] + 后缀
'''
index = old_name.rfind('.') # 找出 . 位于的下标

if index > 0:
    postfix = old_name[index:]

backup_name = old_name[0:index:1] + '[备份]' + postfix # 运用字符串切片规划备份文件名


'''
3.备份文件写入数据
    3.1 打开源文件和备份文件（即创建）
    3.2 将源文件的数据写入备份文件（即源文件读取，备份文件写入）
    3.3 关闭文件
'''
old_f = open(old_name, 'rb') # rb 以二进制读取
backup_f = open(backup_name, 'wb')

# 因为不确定目标备份文件的大小，所以应当循环读取写入，当读取的数据没有了，则中止循环
while True:
    content = old_f.read(1024) # 这里可以填数字，限制读取长度（即备份大小），例如这里限制1024个字节
    if len(content) == 0:
        print('备份完成！')
        break

    backup_f.write(content)

old_f.close()
backup_f.close()



