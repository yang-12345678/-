# -*- coding: utf-8 -*-
# Date: 2021/02/05

from bs4 import BeautifulSoup
import requests

fp = open("test.html", 'r', encoding="utf-8")
soup = BeautifulSoup(fp, 'lxml')
# print(soup)

# print(soup.div)  # 返回第一次出现的标签
# print(soup.find("div"))  # 返回第一次出现的标签
# print(soup.find("div", class_="qin"))  # 属性定位
# print(soup.find_all("a"))
# print(soup.select('.qin'))

