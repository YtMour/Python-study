import requests
#session里面些一些共有的东西
#每一个基于session的请求是独立的
#如果覆盖了共有的东西，就会更新，如果没有就添加

session = requests.Session()
session.headers={'common': 'header','test': 'test'}
html1 = session.get('http://httpbin.org/get',headers={'html1': 'my header'})
print(html1.text)

html2 = session.get('http://httpbin.org/get')
print(html2.text)