# 字符串书写方式
a = ('hello world')
print(a)
print(type(a))
b = "Tom"
print(type(b))

# 三引号书写字符串
c = '''i am Tom'''
print(type(c))

d ="""i am Tom"""
print(type(d))

f = '''i am 
Tom'''
print(f)

'''
书写方式的区别：
1.三（单/双）引号书写支持回车换行，并且不增加任何额外的字符
2.双引号支持 i'm Tom ；而单引号则会报错，解决办法如下
'''
e = 'i\'m Tom' # 想用单引 加一个转义字符 不会报错
print(e)

'''
字符串输出复习
'''
print('hello world')

name = 'Tome'
print('我的名字是%s' % name) # 格式化输出方式1

print(f'我的名字是{name}') # 格式化输出方式2

'''
字符串输入复习
使用 input，input 接收到的数据都是字符串
'''
# 输入密码
password = int(input('请输入您的密码..:'))
print(f'您输入的密码是{password}')
