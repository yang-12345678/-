# -*- coding: utf-8 -*-
# Date: 2021/01/22

import requests

url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

id_list = []  # 存储企业的 id

for page in range(1, 6):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': ''

    }

    json_ids = requests.post(url=url, data=data, headers=headers).json()

    for dic in json_ids['list']:
        id_list.append(dic['ID'])
# print(id_list)

# 获取企业详情数据
post_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
for id in id_list:
    data = {
        'id': id
    }
    detail_json = requests.post(url=post_url, headers=headers, data=data).json()
    print(detail_json)
