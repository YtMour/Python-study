#代理
#403  IP   {}
#更换代理
#免费   失效    测试有效性

# proxies = {
#   'http': 'http://112.250.107.37:53281',
#   'https': 'http://112.250.107.37:53281',
# }

#http://www.ip3366.net/free/?stype=1&page=1
import requests
from bs4 import BeautifulSoup

ips=[]

def verify(proxies):
    url='https://httpbin.org/ip'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
    }
    try:
        html=requests.get(url,proxies=proxies,headers=headers,timeout=3)
        print('状态码：',html.status_code)
        print('IP：',html.text)
        ips.append(proxies)
    except:
        print('代理不可用')

def main():
    for i in range(1,10):
        print('正在爬取页面：',i)
        url=f' {i}'
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cookie': 'Hm_lvt_c4dd741ab3585e047d56cf99ebbbe102=1675665627; Hm_lpvt_c4dd741ab3585e047d56cf99ebbbe102=1675665670',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
        }
        html=requests.get(url,headers=headers)
        soup=BeautifulSoup(html.text,'lxml')
        trs=soup.select('.table.table-bordered tbody tr')
        for tr in trs:
            tds=tr.select('td')[:2]
            for td in tds:
                print(td.text,end=' ')
            IP=tds[0].text
            PORT=tds[1].text
            print('正在验证IP：',IP)
            proxies = {
              'http': f'http://{IP}:{PORT}',
              'https': f'http://{IP}:{PORT}',
            }
            verify(proxies)
            print()
    print('可用代理:',ips)

if __name__ == '__main__':
    main()