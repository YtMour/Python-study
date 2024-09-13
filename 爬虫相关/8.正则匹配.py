"""
DOM HTML  CSS XPATH
JS  CSS   re

.*?  非贪婪匹配
.*  贪婪匹配
"""
import re
import requests

mytext=re.compile('eArea":{"text":"(.*?)"},"excerptA',re.S|re.I|re.M)
mypng=re.compile('"imageArea":{"url":"(.*?)"},"metricsArea"',re.S|re.I|re.M)
myhot=re.compile('"metricsArea":{"text":"(.*?)","fontColor"',re.S|re.I|re.M)

url='https://www.zhihu.com/billboard'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
}
html=requests.get(url,headers=headers)
html.encoding='utf8'

titles=mytext.findall(html.text)
pngs=mypng.findall(html.text)
hot=myhot.findall(html.text)

for title,png,h in zip(titles,pngs,hot):
    print(title)
    print(str(png).replace(r'\u002F','/'))
    print(h)
    #https://picx.zhimg.com/80/v2-4ef85f15104e8adce7928c98bff201d9_1440w.png
    #https:\u002F\u002Fpicx.zhimg.com\u002F80\u002Fv2-d29de6e187849296874ca235336c2521_720w.png
    #b'https://picx.zhimg.com/80/v2-d29de6e187849296874ca235336c2521_720w.png'
