#coded by "Andreas Karageorgos"
#GitHub: https://github.com/AndreasKarageorgos/

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Adds random bytes to the end of every text.
def __pad__(msg):
    if (len(msg)+1)%16==0:
        return msg+"$".encode()+get_random_bytes(16)
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

class simpleAES():

    def __init__(self, key, IV):
        if not isinstance(key,bytes):
            raise Exception("The key must be in bytes")
        elif len(key)!=32:
            raise Exception("The key must be 32 bytes")
        
        if not isinstance(IV,bytes):
            raise Exception("The IV must be in bytes")
        elif len(IV)!=16:
            raise Exception("The IV must be 16 bytes")
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