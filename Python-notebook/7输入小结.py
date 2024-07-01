'''
1.输入 input('提示信息')
2.程序执行到input时，只有用户进行操作了，才会执行下一步
3.input接收到用户输入后，一般存储到变量
4.input会把用户输入的任何信息当作字符串处理！！！
'''

# 1.书写input，观察特点
password = input('请输入您的密码:')
print(f'您输入的密码是{password}')
print(type(password))

# 2.转换数据类型的作用
'''
1.input
2.检测input数据类型
3.int() 转换数据类型
4.检测转换是否成功
'''

num = input('请输入数字:')
print(num)
print(type(num)) # 证明input输入的都存储为str
print(type(int(num))) #int转换

