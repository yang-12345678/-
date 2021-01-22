# -*- coding: utf-8 -*-
# Date: 2021/01/17

import requests

# post 请求 （携带参数）
# 响应数据是一组 json 数据

post_url = "https://fanyi.baidu.com/sug"

# UA 伪装
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

# post 请求参数处理 （同get）
data = {
    'kw': 'dog'
}

response = requests.post(url=post_url, data=data, headers=headers)

# json 方法直接拿到对象 （如果确认服务器响应数据是json,才可以使用）
dic_obj = response.json()
print(dic_obj)
