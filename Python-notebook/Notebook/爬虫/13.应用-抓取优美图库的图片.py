'''
1.拿到主页面的源代码
2.提取每个图片的子链接
3.通过子链接跳转到图片所在页面，最后抓取图片
'''
import os
import requests
import time
import re
from bs4 import BeautifulSoup

# 伪装代码
users_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0', 'Connection':'close'}

# 预载正则表达式
obj = re.compile(r'<strong>(.*?)</strong>', re.S)

# 请求目标主页面
main_url = 'https://www.umeituku.com/bizhitupian/meinvbizhi/'
main_url_resp = requests.get(main_url, headers=users_dict, verify=True)
main_url_resp.encoding = 'utf-8'


# 把源代码交给 bs 再处理, 拿取每个图片对应的子链接
main_url_code = BeautifulSoup(main_url_resp.text, 'html.parser') # html.parser 屏蔽警告
a_list = main_url_code.find('div', class_='TypeList').find_all('a')
child_url_list = []
for a in a_list:
    child_url_list.append(a.get('href'))
main_url_resp.close()


# 根据子链接跳转到图片页面，抓取图片的下载链接
try:
    img_download_url_list = []
    for child_url in child_url_list:
        time.sleep(1)
        child_url_resp = requests.get(child_url, headers=users_dict, verify=True)
        child_url_resp.encoding = 'utf-8'
        child_url_code = BeautifulSoup(child_url_resp.text, 'html.parser')
        single_img_download_url = [] # 存储每张图片的名字和下载链接
        title = str(child_url_code.find('div', class_='ArticleTitle').find('strong'))
        img = child_url_code.find('div', class_='ImageBody').find('img')
        img_name = obj.findall(title)[0]
        single_img_download_url.append(img_name)
        print(f'正在抓取 {img_name} 的下载链接...')
        single_img_download_url.append(img.get('src'))
        img_download_url_list.append(single_img_download_url)
        child_url_resp.close()
    print('所有图片的下载链接抓取完毕...')


    # 下载图片
    print('')
    print('开始下载图片...')
    os.mkdir('美女图片')
    os.chdir('美女图片')
    for single_img_download_url in img_download_url_list:
        time.sleep(1)
        img_download_url_resp = requests.get(single_img_download_url[1], headers=users_dict, verify=True)
        f = open(single_img_download_url[0] + '.jpg', 'wb')
        f.write(img_download_url_resp.content) # 写入目标文件字节流
        f.close()
        img_download_url_resp.close()
        print(f'图片 {single_img_download_url[0]} 下载完成...')

    print('所有图片下载完成...')
except:
    print('爬取中断，已保存已经爬取的内容...')



