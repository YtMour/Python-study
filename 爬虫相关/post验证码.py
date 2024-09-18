import requests
import ddddocr
from urllib.parse import quote
import random

def get_ocr():
    ocr=ddddocr.DdddOcr()
    with open('code.jpg','rb') as f:
        img=f.read()

    res = ocr.classification(img)
    print(f'识别结果：{res}')
    return res

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'Referer': 'http://www.efnchina.com/index.php?m=member&c=index&a=login&forward=http%3A%2F%2Fwww.efnchina.com%2F&siteid=1',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}

session=requests.session()
session.headers=headers
url='http://www.efnchina.com/api.php?op=checkcode&code_len=5&font_size=14&width=120&height=26&font_color=&background=&'+str(random.random())

html=session.get(url)
with open('code.jpg', 'wb') as f:
    f.write(html.content)

PHPSESSID=html.headers['Set-Cookie'].split(';')[0]
headers['Cookie']=PHPSESSID
headers['Content-Type']='application/x-www-form-urlencoded'
data={
    'forward': quote('http://www.efnchina.com/'),
    'username': 'xjb8888',
    'password': 'xjb8888',
    'code': str(get_ocr()),
    'cookietime': '2592000',
    'dosubmit': quote('登录')
}


url='http://www.efnchina.com/index.php?m=member&c=index&a=login&forward=http%3A%2F%2Fwww.efnchina.com%2F&siteid=1'
html=session.post(url,headers=headers,data=data)
print(html.text)