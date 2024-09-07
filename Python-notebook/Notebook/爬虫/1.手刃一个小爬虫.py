'''
爬虫定义：通过编写程序来获取到互联网上的资源

爬虫满足的需求：用程序模拟浏览器，输入一个网址，从该网址中获取资源或内容

'''
from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url) # 获取目标页面的源代码

# print(resp.read().decode('utf-8')) -- 使用 .read() 方法打印读取的内容；使用 decode() 解码

with open('mybaidu.html', 'w', encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))

f.close()

print('over...')