import requests
from bs4 import BeautifulSoup


url = 'https://www.baidu.com/s?wd=中秋节'
headers = {
    'Cookie': 'BAIDUID=C03E703F930D7D0F4D777D7D0D9D0D9D:FG=1; BIDUPSID=C03E703F930D7D0F4D777D7D0D9D0D9D; PSTM=1517139272; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; H_PS_PSSID=1435_21111_21059_21111_21111_211',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

html = requests.get(url, headers=headers)
html.encoding = 'utf-8'
# print(html.text)

soup = BeautifulSoup(html.text, 'lxml')
requests=soup.select('div.c-container.xpath-log.new-pmd h3 a')
for r in requests:
    print(r.text.replace('\n','').replace(' ',''),r['href'])
