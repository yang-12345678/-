# -*- coding: utf-8 -*-
# Date: 2021/01/15

import requests
# 爬取搜狗首页的页面数据

# 1、指定 url
url = "https://www.sougou.com/"

# 2、发起请求
response = requests.get(url)

# 3、获取响应数据
pop_text = response.text  # .text属性返回的是字符串形式的相应数据
print(pop_text)

# 4、持久化存储
with open(".sougou.html", 'w', encoding='utf-8') as f:
    f.write(pop_text)
