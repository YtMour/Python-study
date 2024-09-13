"""
列表页  翻页  URL 标题
详情页  内容

https://www.lz13.cn/lizhi/lizhimingyan-35.html
https://www.lz13.cn/lizhi/lizhimingyan-34.html
https://www.lz13.cn/lizhi/lizhimingyan-33.html
...
https://www.lz13.cn/lizhi/lizhimingyan-1.html
"""

import requests
from bs4 import BeautifulSoup
import os

def secondSpider(url,title):
    html = requests.get(url)
    html.encoding = 'utf8'
    soup = BeautifulSoup(html.text, 'lxml')
    postHeader = soup.select('.PostContent p')[0]
    print('名言内容：',postHeader.text)

    if not os.path.exists('./content'):
        os.mkdir('./content')

    with open(f'./content/{title}.txt','a+',encoding='utf8')as f:
        f.write(postHeader.text)

def firstSpider(url):
    html = requests.get(url)
    html.encoding = 'utf8'
    soup = BeautifulSoup(html.text, 'lxml')
    postHeader = soup.select('div#node-8890 .PostHead')
    # 列表页
    for ph in postHeader:
        innerUrl = ph.select('span h3 a')[0]['href']
        title = ph.select('span h3 a')[0].text
        print(f'标题：{title} url：{innerUrl}')
        secondSpider(innerUrl,title)

def main():
    # 翻页
    for i in range(1, 2):
        url = f'https://www.lz13.cn/lizhi/lizhimingyan-{i}.html'
        print('当前爬取的网页URL：', url)
        firstSpider(url)

if __name__ == '__main__':
    main()