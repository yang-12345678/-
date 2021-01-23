# -*- coding: utf-8 -*-
# Date: 2021/01/23

import requests

url = "https://pic.qiushibaike.com/system/pictures/12400/124006644/medium/05390SOTI1H6WRGJ.jpg"
response = requests.get(url=url).content  # 返回二进制形式的数据

with open("qiutu.jpg", "wb") as f:
    f.write(response)
