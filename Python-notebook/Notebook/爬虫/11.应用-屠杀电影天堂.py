'''
1.定位到电影天堂必看电影的首页，抓取页脚处的总页数
2.根据总页数+range()+字符串拼接，拼接出每一页的链接
3.定位到每一页的链接，抓取每一页所有电影的子链接
4.根据电影子链接抓取每一个电影介绍页面的名字、评分和种子链接
'''
import time
import requests
import re

f = open('种子.txt', 'w', encoding='utf-8')

# 伪装代码
users_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0', 'Connection':'close'}


# 预加载正则表达式
obj = re.compile(r"下一页</a>&nbsp;&nbsp;<a href='/html/bikan/index_(\d+).html'>尾页", re.S)
obj1 = re.compile(r'<td height="26">.*?<a href="(?P<movie_url>.*?)" class="ulink"', re.S)
obj2 = re.compile(r'<br />◎片　　名(?P<Name>.*?)<br />.*?◎豆瓣评分(?P<Douban_rating>.*?)<br />.*?<tbody>.*?<a href="(?P<Seed>.*?)">', re.S)


# 计算页码数
url = 'https://www.dytt89.com/html/bikan/'
resp = requests.get(url, headers=users_dict, verify=False)
resp.encoding = 'gb2312'
result = obj.findall(resp.text)
resp.close()
page_count = eval(result[0])


# 准备所有页码链接
page_url_list = []
page_url_list.append(url)
for i in range(2, page_count+1):
    page_url = 'https://www.dytt89.com/html/bikan/index_' + str(i) + '.html'
    page_url_list.append(page_url)


# 跳转到对应页面并获取各电影页面子链接
movie_url_list = []
for page_url in page_url_list:
    time.sleep(1)
    page_resp = requests.get(page_url, headers=users_dict, verify=False)
    page_resp.encoding = 'gb2312'
    page_code = page_resp.text
    page_resp.close()
    result1 = obj1.finditer(page_code)
    for item1 in result1:
        movie_url_list.append('https://www.dytt89.com' + item1.group('movie_url'))


# 抓取电影的名字、评分和下载种子
try:
    for movie_url in movie_url_list:
        time.sleep(1)
        movie_url_resp = requests.get(movie_url, headers=users_dict, verify=False)
        movie_url_resp.encoding = 'gb2312'
        movie_url_code = movie_url_resp.text
        movie_url_resp.close()
        result2 = obj2.finditer(movie_url_code)
        for item2 in result2:
            dict = item2.groupdict()
            dict['Name'] = dict['Name'].strip('\u3000')
            dict['Douban_rating'] = dict['Douban_rating'].strip('\u3000')
            print(f"正在抓取{dict['Name']}的相关信息...")
            lt = list(dict.items())
            lt1 = []
            for m in lt:
                lt1.append('{}:{}'.format(m[0], m[1]))
            print(lt1)
            f.write(','.join(lt1) + '\n')
    f.close()
    print('所有数据抓取完毕...')
except:
    print('请求错误，已保存抓取到的信息...')
    f.close()