from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 生成秘钥
# key=RSA.generate(2048)
# with open('public.pem','wb')as f:
#     public_key=key.public_key().export_key()
#     f.write(public_key)
# with open('private.pem', 'wb') as f:
#     private_key=key.export_key()
#     f.write(private_key)

def encrypt_rsa(data):
    """使用公钥对数据进行RSA加密。"""
    my_key=RSA.import_key(open('public.pem','rb').read())
    rsa=PKCS1_OAEP.new(my_key)
    res=rsa.encrypt(data)
    print('解密结果：',res)
    return res

def decrypt_rsa(data):
    """使用私钥对数据进行RSA解密。"""
    my_key = RSA.import_key(open('private.pem','rb').read())
    rsa = PKCS1_OAEP.new(my_key)
    res = rsa.decrypt(data)
    print('加密结果：', res.decode())
    return res

if __name__ == '__main__':
    # 主执行部分，用于加密数据然后解密
    data="ytmour".encode()
    res=encrypt_rsa(data)
    decrypt_rsa(res)

