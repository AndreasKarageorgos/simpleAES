#coded by "Andreas Karageorgos"
#GitHub: https://github.com/AndreasKarageorgos/

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256, md5

#Adds random bytes to the end of every text.
def __pad__(msg):
    if (len(msg)+1)%16==0:
        return msg+"$".encode()+get_random_bytes(16)
    elif (len(msg)+2)%16==0:
        return msg+"$".encode()+get_random_bytes(17)
    else:
        remain = 16 - (len(msg)%16)
    return msg+"$".encode()+get_random_bytes(remain-1)

#Removes the extra bytes from the original text.
def __unpad__(msg):
    msg = msg.split("$".encode())[:-1]
    return b"$".join(msg)

#Generates and returns 32 random bytes that can be used for the key.
def keyGenerator():
    return get_random_bytes(32)

#Generates and returns 16 random bytes that can be used for the IV
def ivGenerator():
    return get_random_bytes(16)

def loadKeyFromFile(path):
    with open(path,"rb") as f:
        data = f.read()
        f.close()
    key=data[:32]
    iv=data[32:]
    return (key,iv)

class simpleAES():

    def __init__(self, key, IV, hash=False, salt="".encode()):
        if (not isinstance(key, bytes)) or (not isinstance(IV, bytes)):
            raise ValueError("The key and IV must be in bytes")
        if hash:
            self.key = sha256(key).digest()
            self.iv = md5(key+salt).digest()
        else:
            if len(key)!=32:
                raise ValueError("The key must be 32 bytes long")
            if len(IV)!=16:
                raise ValueError("The IV must be 16 bytes long")
            self.key = key
            self.iv = IV
    
    def encrypt(self, plaintext):
        if not isinstance(plaintext, bytes):
            raise Exception("The plaintext must be in bytes")
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        pad_plaintext = __pad__(plaintext)
        return cipher.encrypt(pad_plaintext)
        
    def decrypt(self, ciphertext):
        if not isinstance(ciphertext, bytes):
            raise Exception("The ciphertext must be in bytes")
        if len(ciphertext)%16!=0:
            raise Exception("Unknown ciphertext")
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        plaintext = cipher.decrypt(ciphertext)
        return __unpad__(plaintext)

    def extractKey(self, path):
        with open(path, "wb") as f:
            f.write(self.key+self.iv)
            f.close()