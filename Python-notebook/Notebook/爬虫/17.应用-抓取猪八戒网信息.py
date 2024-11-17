'''
1.拿取页面源代码
2.提取和解析数据
'''
import requests
from lxml import etree

# 伪装代码
users_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0', 'Connection':'close'}

# 获取目标页面源代码
url = 'https://www.zbj.com/fw/?k=saas'

try:
    f = open('saas.txt', 'r', encoding='gb18030')
    page_content = f.read()
    f.close()

    # 解析数据
    tree = etree.HTML(page_content)
    # 根据规律拿取每一个服务商的 div
    divs = tree.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div')
    single_info = []
    all_info = []
    for div in divs:
        price = div.xpath('./div/div[@class="bot-content"]/div[@class="price"]/span/text()') # 提取价格
        pre_name = div.xpath('./div/div[@class="bot-content"]/div[@class="name-pic-box"]/a/span//text()') # 提取服务名称
        company = div.xpath('./div/div/div/div/div/text()') # 提取企业名称
        name = ''
        for word in pre_name: # 重新拼接名称
            word = word.strip(' ')
            name += word
        single_info.append(name)
        single_info.append(price[0])
        single_info.append(company[0])
        all_info.append(single_info)
        single_info = []

    # 信息按照价格进行升序排列
    all_info.sort(key=lambda x:eval(x[1].strip('¥')), reverse=False)

    # 保存信息
    f1 = open('zbj_saas_info.txt', 'w', encoding='utf-8')
    print('开始保存信息...')
    for info in all_info:
        f1.write(','.join(info) + '\n')
    print('信息保存完毕...')
    f1.close()
except:
    resp = requests.get(url, headers=users_dict, verify=False)
    origin_page_content = resp.text
    f = open('saas.txt', 'w', encoding='gb18030')
    f.write(origin_page_content)
    f.close()
    print('页面源代码抓取成功，请再次运行...')
    resp.close()
