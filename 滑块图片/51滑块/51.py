import requests
import re
from PIL import Image
import time
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
from base64 import b64decode,b64encode

key='dadc8ec933f061ab73076bb47058604d'[:16].encode()
iv='1234577290ABCDEF1264147890ACAE45'[:16].encode()

def encrypt_cbc(data):
    aes=AES.new(key,AES.MODE_CBC,iv=iv)
    res=aes.encrypt(pad(data.encode(),16))
    print('AES-CBC:',b64encode(res).decode())
    return b64encode(res).decode()

big_img_re=re.compile('background-image: url(.*?);',re.S|re.I)
pos_re=re.compile("class='gt_cut_fullbg_slice' style='background-position:(.*?)px (.*?)px",re.S|re.I)
challenge_re=re.compile('id="challenge" value="(.*?)">',re.S|re.I)
times_re=re.compile('id="times" value="(.*?)">',re.S|re.I)


def get_time():
    return str(int(time.time()*1000))


def save_img(url):
    img=requests.get(url).content
    with open('img.png','wb') as f:
        f.write(img)
    print('Image saved.')

def get_img():
    url = "https://authcode.51.com/authcode/slidecode"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

    html=requests.get(url,headers=headers)

    imgs=big_img_re.findall(html.text)

    if imgs:
        big_img='https:'+imgs[0].replace('("','').replace('")','')
        print('Big image url:',big_img)
    else:
        print("No big image found.")

    save_img(big_img)

    #获取坐标xy
    position=pos_re.findall(html.text)
    position=[[abs(int(pos[0].replace(' ',''))),
                abs(int(pos[1].replace(' ','')))]
                for pos in position]
    print(position,len(position))

    #获取必要参数
    challenge=challenge_re.findall(html.text)[0]
    times=times_re.findall(html.text)[0]
    print('challenge:',challenge)
    print('times:',times)

    my_img=Image.open('./img.png')
    crop_list=[]

    for p in position:

        if p[1]==0:
            crop_list.append(my_img.crop((p[0],0,p[0]+13,25)))
        if p[1]==25:
            crop_list.append(my_img.crop((p[0],25,p[0]+13,50)))
        if p[1]==50:
            crop_list.append(my_img.crop((p[0],50,p[0]+13,75)))
        if p[1]==75:
            crop_list.append(my_img.crop((p[0],75,p[0]+13,100)))

    new_img=Image.new('RGB',(260,100))
    x_offset=0
    y_offset=0

    for crop in crop_list:
        if x_offset==260:
            x_offset=0
            y_offset+=25
        new_img.paste(crop,(x_offset,y_offset))
        x_offset+=13

    new_img.save('./new_img.png')

    # 识别过程 图像识别
    point = 14

    params = {
        # 'callback': f'jQuery111105988221727827756_{get_time()}',
        'point': point,
        'times': times,
        'challenge': challenge,
        'token': md5((str(challenge) + str(times) + str(point)).encode()).hexdigest(),
        # md5(challenge + timestamp + _x)
        'from': 'www',
        'divpre': '',
        '_': get_time()
    }
    url = 'https://authcode.51.com/authcode/yz2'
    html = requests.get(url, params=params, headers=headers)
    print(html.json())

    url = 'https://passport.51.com/login/submit'
    params = {

        'passport_51_user': encrypt_cbc('15936966600'),
        'passport_51_password': encrypt_cbc('15936966600'),
        'passport_cookie_login': '0',
        'from': 'www',
        'gourl': '//www.51.com',
        'passport_auto_login': '1',
        'passport_51_ishidden': '0',
        'identifier': challenge,
        'passport_51_authcode': point,
        'chn': 'www',
        'ie': '0',
        'version': '2012',
        'passport_51_ajax': 'true',
        'passport_51_jsonp': '1',
        'aes': '2',
        'passport_51_user_ht': '18',
        'passport_51_password_ht': '18',
        '_': get_time()
    }
    html = requests.get(url, params=params, headers=headers)
    print(html.json())


if __name__ == '__main__':
    get_img()


