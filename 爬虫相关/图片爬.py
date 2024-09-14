"""
AJAX 异步加载  瀑布流
URL没有变化  内容却不断更新
XHR请求     JSON（中间语言）   dict

{"antiFlag":1,"message":"Forbid spider access","bfe_log_id":"11768782920408771089"}
{"antiFlag":1,"message":"Forbid spider access","bfe_log_id":"12078284916214976827"}

anti 反  anti_content
spider  crawler 爬虫
"""
import requests
import os
url='https://image.baidu.com/search/acjson'
headers={
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
    'Cookie': 'BDqhfp=%E6%B1%BD%E8%BD%A6%26%26NaN-1undefined%26%260%26%261; indexPageSugList=%5B%22python%22%2C%22%E9%BB%91%E5%AE%A2%22%2C%22%E5%AE%89%E5%85%A8%22%2C%22%E9%80%86%E5%90%91%22%5D; PSTM=1670679924; BAIDUID=2C1FC9C9929E533A115F5A90621F6B92:FG=1; BIDUPSID=5B1DFD3B99B5065DF1522F28819214A1; H_PS_PSSID=37858_36555_37961_37910_37832_37872_37793_37949_37928_37758_37902_26350_37788_37881; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=2C1FC9C9929E533A115F5A90621F6B92:FG=1; delPer=0; PSINO=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; ab_sr=1.0.1_OGJiZGU5YTYwMGQwNzg5NmMwN2M4OWU2ODIwOWFhMDAxZTVhY2E2Y2JmY2MyZTVlNGZlZDM3YmRkZmM1ZThhMjI5MDY4NzAzMTRkMTEzZWYxNzc4YzFjMDJmYWI0NzA5YmE4NWM1MDBiNDY1NDM1YzZlZDljYjRiNmFiYWM0NGMzZmNiZjUzODJiYjhmZDMyNjE0ZjQzOTgwNmM2YTA4Zg==',
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDYsMSw1LDQsNywyLDgsOQ%3D%3D&word=%E6%B1%BD%E8%BD%A6',
}
pagenumber =30
for i in range(2):
    params={
        'tn': 'resultjson_com',
        'word':'汽车',
        'queryWord':'汽车',
        'pn': str(pagenumber),
        'rn': '30'
    }
    pagenumber+=30
    html=requests.get(url,params=params,headers=headers)
    for i in html.json()['data']:
        if i:
            title=i['fromPageTitle']
            img=i['thumbURL']
            print(i['thumbURL'])

            if not os.path.exists('./baiduimgs'):
                os.mkdir('./baiduimgs')

            with open(f'./baiduimgs/{title}.png', 'wb') as f:
                f.write(requests.get(img).content)