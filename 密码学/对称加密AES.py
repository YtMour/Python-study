from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

key = get_random_bytes(16)
iv = get_random_bytes(16)
nonce=get_random_bytes(8)

def encrypt_ecb(data):
        # 确保数据长度为16的倍数
        """
        使用AES ECB模式对数据进行加密，并返回Base64编码后的密文。
        """
        padded_data = pad(data, AES.block_size)
        aes = AES.new(key, AES.MODE_ECB)
        res = aes.encrypt(padded_data)
        print(res)
        print(b64encode(res).decode())
        return b64encode(res).decode()



def decrypt_ecb(data):
    """
    使用AES ECB模式对Base64编码的密文进行解密，并输出明文。
    """
    aes= AES.new(key, AES.MODE_ECB)
    res = aes.decrypt(b64decode(data.encode()))
    print(unpad(res,16).decode())





def encrypt_cbc(data):
    """
    使用AES CFB模式对数据进行加密，并返回Base64编码后的密文。
    """
    aes=AES.new(key,AES.MODE_CFB,iv=iv)
    res=aes.encrypt(pad(data,16))
    print(b64encode(res).decode())
    return b64encode(res).decode()

def decrypt_cbc(data):
    """
    使用AES CFB模式对Base64编码的密文进行解密，并输出明文。
    """
    aes = AES.new(key, AES.MODE_CFB,iv=iv)
    res = aes.decrypt(b64decode(data.encode()))
    print(unpad(res,16).decode())



def encrypt_ctr(data):
    """
    使用AES CTR模式对数据进行加密，并返回Base64编码后的密文。
    """
    aes=AES.new(key,AES.MODE_CTR,nonce=nonce)
    res=aes.encrypt(pad(data,16))
    print(b64encode(res).decode())
    return b64encode(res).decode()

def decrypt_ctr(data):
    """
    使用AES CTR模式对Base64编码的密文进行解密，并输出明文。
    """
    aes = AES.new(key, AES.MODE_CTR,nonce=nonce)
    res = aes.decrypt(b64decode(data.encode()))
    print(unpad(res,16).decode())




if __name__ == '__main__':
    data = 'ytmour'.encode()
    res=encrypt_ctr(data)
    decrypt_ctr(res)
