import os
import requests
import time
import re
from bs4 import BeautifulSoup

# 伪装代码
users_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0', 'Connection':'close'}

# 预载正则表达式
obj = re.compile(r'<h1>(.*?)</h1>', re.S)

# 请求目标主页
main_url = 'https://www.laowangidol.cc/category/%e5%81%b6%e5%83%8f%e5%86%99%e7%9c%9f/'
main_url_resp = requests.get(main_url, headers=users_dict, verify=False)
main_url_resp.encoding = 'utf-8'


# bs4 处理，获取首页写真栏目的子链接
main_url_code = BeautifulSoup(main_url_resp.text, 'html.parser')
a_list = main_url_code.find('div', class_='article-list col-row clr').find_all('a', class_='item-img')
main_url_resp.close()
child_url_list = []
for a in a_list:
    child_url_list.append(a.get('href'))


# 根据子链接跳转到图片页面，抓取图片的下载链接
img_download_url_list = []
for child_url in child_url_list:
    time.sleep(1)
    child_url_resp = requests.get(child_url, headers=users_dict, verify=False)
    child_url_resp.encoding = 'utf-8'
    child_url_code = BeautifulSoup(child_url_resp.text, 'html.parser')
    img_name = str(child_url_code.find('div', id='breadcrumbs').find('h1'))
    img_name = obj.findall(img_name)[0]
    img_list = child_url_code.find('div', class_='single-text').find_all('img', decoding='async')
    single_img_download_url_list = []
    single_img_download_url_list.append(img_name)
    for img in img_list:
        single_img_download_url_list.append(img.get('src'))
    img_download_url_list.append(single_img_download_url_list)
    print(f'正在抓取 {img_name} 的图片下载链接...')
    child_url_resp.close()
print('所有图片的下载链接抓取完毕...')

top_level_folder = os.getcwd()
# 下载图片
print('')
print('开始下载图片...')
for single_img_download_url_list in img_download_url_list:
    os.mkdir(single_img_download_url_list[0])
    os.chdir(single_img_download_url_list[0])
    img_num = 1
    for img_download_url in single_img_download_url_list[1:]:
        time.sleep(1)
        img_download_url_resp = requests.get(img_download_url, headers=users_dict, verify=True)
        f = open(str(img_num) + '.jpg', 'wb')
        f.write(img_download_url_resp.content)
        f.close()
        img_num += 1
        img_download_url_resp.close()
    print(f'{single_img_download_url_list[0]} 下载完成...')
    os.chdir(top_level_folder)
print('所有任务图片下载完成...')





