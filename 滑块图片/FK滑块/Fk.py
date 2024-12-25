import requests
from base64 import b64decode
import py_mini_racer
import json

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
  validateSign=html['msg']['validateSign']
  print('validateSign:',validateSign)

else:
  print("请求图片失败:",html['msg'])

with open('fk.png','wb') as f:
  f.write(b64decode(bs64img))
  print("图片已保存到当前目录")
  f.close()


def get_vi():
    with open('fk.js','r',encoding='utf-8')as f:
        ctx=py_mini_racer.MiniRacer()
        ctx.eval(f.read())
        args={"s":10,
              "l":54,
              "dy":524,
              "uy":524,
              "t":[[562,15,1680446604024,0,0],[381,458,1680446604524,0,0],[376,524,1680446605026,0,0],
                   [376,524,1680446605164,1,1],
                   [376,524,1680446605166,2,1],[377,524,1680446605217,2,1],[378,524,1680446605221,2,1],[380,524,1680446605225,2,1],[382,524,1680446605229,2,1],[384,524,1680446605233,2,1],[388,524,1680446605237,2,1],[390,524,1680446605241,2,1],[394,524,1680446605245,2,1],[396,524,1680446605249,2,1],[400,524,1680446605253,2,1],[402,524,1680446605257,2,1],[406,524,1680446605261,2,1],[408,524,1680446605265,2,1],[412,524,1680446605269,2,1],[414,524,1680446605273,2,1],[416,524,1680446605277,2,1],[418,524,1680446605281,2,1],[419,524,1680446605285,2,1],[420,524,1680446605287,2,1],[420,524,1680446605291,2,1],[421,524,1680446605299,2,1],[422,524,1680446605323,2,1],[422,524,1680446605331,2,1],[423,524,1680446605339,2,1],[424,524,1680446605347,2,1],[424,524,1680446605355,2,1],[425,524,1680446605363,2,1],[426,524,1680446605379,2,1],[426,524,1680446605387,2,1],[427,524,1680446605391,2,1],[428,524,1680446605395,2,1],[428,524,1680446605403,2,1],[429,524,1680446605411,2,1],[430,524,1680446605431,2,1],
                   [430,524,1680446605517,3,1]],
              "validateSign":validateSign}
        result=ctx.call('get_vi',json.dumps(args))
        print('vi:',result)
        return result

url='https://cv.fkw.com/verify/validate'\

data={
    "appKey": 1,
    "et": 6,
    "bss": 4,
    "bssKey": "ALihhLoGCAEQBBoHWzEsMyw1XSIJ6ZKf55Sz5qC5",
    "version": "1.0.1",
    "vi": get_vi(),
}
html=requests.post(url,headers=headers,json=data)
