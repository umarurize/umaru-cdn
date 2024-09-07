import requests

url = 'https://movie.douban.com/j/chart/top_list'

# 如果使用 get 请求得到的 url 参数过多，可以考虑重新封装参数
params_dict = {'type': '24', 'interval_id': '100:90', 'action': '', 'start': 20, 'limit': 20}

# 伪装代码
user_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}


resp = requests.get(url, params=params_dict, headers=user_dict)

print(resp.text)

# 关闭响应
resp.close()
