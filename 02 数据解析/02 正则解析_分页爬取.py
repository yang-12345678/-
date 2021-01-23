# -*- coding: utf-8 -*-
# Date: 2021/01/23

# 需求：爬取糗事百科中糗图模块下所有的糗图
import requests
import re
import os

# 创建一个文件夹，保存所有的图片
if not os.path.exists("qiutuLibs"):
    os.mkdir("qiutuLibs")

url = "https://www.qiushibaike.com/imgrank/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

page_text = requests.get(url=url, headers=headers).text

ex = "<div class=\"thumb\">.*?<img src=\"(.*?)\" alt.*?</div>"

img_src_list = re.findall(ex, page_text, re.S)
# print(img_src_list)

for src in img_src_list:
    # 拼接 url
    src = "https:" + src
    img_data = requests.get(url=src, headers=headers).content

    # 生成图片名称
    img_name = src.split('/')[-1]
    # 图片最终存储路径
    img_Path = "qiutuLibs/" + img_name

    with open(img_Path, "wb") as f:
        f.write(img_data)
        print(img_name, "下载成功！")

input()
