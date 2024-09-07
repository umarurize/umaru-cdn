import requests

query = input('请输入一个明星的名字：')

url = f'https://www.sogou.com/web?query={query}'

# resp = requests.get(url)

# print(resp.text) 此验证码用于确认这些请求是您的正常行为而不是自动程序发出的，需要您协助验证 -- 服务器识别到使用爬虫工具请求，被拦截，所以要对代码进行伪装

# 伪装程序，简单处理反爬
dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}

resp = requests.get(url, headers=dict)

print(resp.text) # 获得目标页面源代码

resp.close()
