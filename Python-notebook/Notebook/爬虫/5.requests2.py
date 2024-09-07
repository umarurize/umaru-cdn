'''
需求：获取百度翻译的结果
'''
import requests

url = 'https://fanyi.baidu.com/sug'

target_word = input('请输入想要翻译的英文单词：')
data_dict = {'kw': target_word}

resp = requests.post(url, data=data_dict)
print(resp.json())

resp.close()

