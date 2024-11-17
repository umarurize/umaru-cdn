'''
模拟用户登录的步骤
    1.登录 -- 处理 cookie
    2.带着 cookie 去请求目标页面的 url，从而请求到书架上的内容

    以上两个操作在实际应用中要结合起来，需要使用 session 请求，session 可以认为是一连串的请求，在请求过程中，cookie 不会丢失
'''

import requests
from lxml import etree

# 伪装代码
users_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0', 'Connection':'close'}

# 跳转到我的资源页面
try:
    f = open('minebbs_umaru.txt', 'r', encoding='utf-8')
    page_content = f.read()
    f.close()

    #解析数据
    tree = etree.HTML(page_content)
    divs = tree.xpath('//*[@id="top"]/div[3]/div[2]/div[3]/div/div/div[1]/div/div[2]/div/div/div')
    single_info_dict = {}
    all_info = []
    for div in divs:
        pre_name = div.xpath('./div[2]/div[1]/a[1]/text()')
        version = div.xpath('./div[2]/div[1]/span[3]/text()')
        name = pre_name[0] + version[0]
        description = div.xpath('./div[2]/div[3]/text()')
        price = div.xpath('./div[2]/div[1]/a[2]/span/text()')
        single_info_dict['name'] = name
        single_info_dict['description'] = description[0]
        single_info_dict['price'] = price[0]
        all_info.append(single_info_dict)
        single_info_dict ={}
    print(all_info)
except:
    # 登录
    session = requests.session()
    account = {'login': 'umaru', 'password': '1329420890lxaa'}
    login_url = 'https://www.minebbs.com/login/login'
    session.post(login_url, headers=users_dict, verify=False, data=account)
    session.close()

    # 将页面源代码写入 txt 中，避免二次访问
    page_url = 'https://www.minebbs.com/resources/authors/umaru.3812/'
    resp = session.get(page_url, headers=users_dict, verify=False)
    resp.close()
    f = open('minebbs_umaru.txt', 'w', encoding='utf-8')
    f.write(resp.text)
    f.close()
    print('页面源代码抓取成功，请再次运行...')


