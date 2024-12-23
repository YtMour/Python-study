import requests
from base64 import b64decode


url='https://cv.fkw.com/verify/get'
data={
  "bss": 4,
  "bssKey": "ALihhLoGCAEQBBoHWzEsMyw1XSIJ6ZKf55Sz5qC5",
  "appKey": 1,
  "version": "1.0.1"
}

headers={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

html=requests.post(url,headers=headers,json=data).json()
if html['success']:
  bs64img=html['msg']['imgId']

else:
  print("请求图片失败:",html['msg'])

with open('fk.png','wb') as f:
  f.write(b64decode(bs64img))
  print("图片已保存到当前目录")
  f.close()

