import re
import requests

m3u8_url=re.compile('e":"","url":"(.*?)","url',re.S|re.I|re.M)
url='https://www.olevod.com/index.php/vod/play/id/41175/sid/1/nid/1.html'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
    'referer': 'https://www.olevod.com/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}
session=requests.Session()
session.headers=headers

#正则获取m3u8的URL
html=session.get(url)
m3u8=m3u8_url.findall(html.text)[0].replace('\\','')
#请求第一个M3U8
html2=session.get(m3u8)
url3='https://europe.olemovienews.com/ts2/20230323/Jzejzcfv/mp4/Jzejzcfv.mp4/'
for i in html2.text.split('\n'):
    if 'm3u8' in i and '#' not in i:
        #print(i)
        url3+=str(i)

#https://europe.olemovienews.com/ts2/20221215/oltwmptd/mp4/oltwmptd.mp4/index-v1-a1.m3u8
#index-v1-a1.m3u8
ts=[]
#seg-1-v1-a1.ts
#https://europe.olemovienews.com/ts2/20221215/oltwmptd/mp4/oltwmptd.mp4/seg-10-v1-a1.ts
html3=session.get(url3)
for i in html3.text.split('\n'):
    if 'ts' in i and '#'not in i:
        ts.append('https://europe.olemovienews.com/ts2/20230323/Jzejzcfv/mp4/Jzejzcfv.mp4/'+str(i))


for num,t in enumerate(ts):
    html4=session.get(t)
    with open('阿凡达.mp4','ab+')as f:
        f.write(html4.content)
        print('已经写入第{}个，一个{}个，进度{}%'.format((num+1),len(ts),((num+1)/len(ts))))