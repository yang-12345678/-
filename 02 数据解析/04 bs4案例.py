
# Date: 2021/02/05

# 需求：爬取三国演义小说所有的章节标题和章节内容
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

url = "https://www.shicimingju.com/book/sanguoyanyi.html"

page_text = requests.get(url=url, headers=headers).text.encode('iso-8859-1').decode('utf-8')

# 在首页中解析出章节标题和详情页的 url
soup = BeautifulSoup(page_text, 'lxml')
# 解析章节标题和详情页的 url
li_list = soup.select(".book-mulu > ul > li")
with open("sanguo.txt", "w", encoding="utf-8") as f:
    for li in li_list:
        title = li.a.string
        detail_url = "https://www.shicimingju.com" + li.a['href']
        detail_page_text = requests.get(url=detail_url, headers=headers).text.encode('iso-8859-1').decode('utf-8')
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find("div", class_="chapter_content")
        content = div_tag.text
        print(content)
        f.write(title + ":" + content + "\n")
        print(title + "   爬取成功！")
