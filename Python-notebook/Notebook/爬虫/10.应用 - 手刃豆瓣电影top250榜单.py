import requests
import re

url = 'https://movie.douban.com/top250'

# 伪装代码
users_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}

# 获取目标页面源代码
resp = requests.get(url, headers=users_dict)
page_content = resp.text

# 预加载正则表达式
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?'
                 r'<span class="rating_num" property="v:average">(?P<rating>.*?)</span>.*?<span>(?P<people_num>.*?)人评价</span>.*?</li>', re.S)

# 正则筛选，返回迭代器
result = obj.finditer(page_content)

# 写入数据
f = open('top250_data.txt', 'w', encoding='utf-8')

for item in result:
    dict = item.groupdict()
    dict['year'] = dict['year'].strip()
    lt = list(dict.items())
    lt1 = []
    for i in lt:
        lt1.append('{}:{}'.format(i[0], i[1]))
    f.write(','.join(lt1) + '\n')

f.close()
resp.close()