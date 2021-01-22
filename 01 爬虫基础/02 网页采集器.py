# -*- coding: utf-8 -*-
# Date: 2021/01/17

import requests

# UA:User-Agent (请求载体的身份标识)
# 反爬机制
# UA检测：门户网站的服务器会检测对应请求载体的身份标识
#       如果检测到为某一款浏览器，则正常，否则为不正常（爬虫），不正常则服务器拒绝请求

# UA 伪装：反反爬策略，让爬虫的身份标识伪装成 浏览器

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

url = "https://www.sogou.com/web?"
# 处理 url 携带的参数：封装到字典中
kw = input("enter a word:")
param = {
    "query": kw
}

# 对指定的 url 发起的请求对应的 url 是携带参数的，并且请求的过程中处理了参数
response = requests.get(url=url, params=param, headers=headers)

page_text = response.text
print(page_text)
fileName = kw + ".html"
with open(fileName, "w", encoding="utf-8") as f:
    f.write(page_text)
    print(fileName + "保存成功")
