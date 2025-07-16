# Simple AES

Find more information about this library [HERE](https://sites.google.com/view/simpleaes/)

An easy way to use the aes CBC mode of pycryptodome.
To use this library just type:

    pip install pycryptosimple-aes

# Code examples

## Automated key generation:

    from pycryptosimple_aes import *

    key = keyGenerator()
    IV = ivGenerator()

    aes = simpleAES(key, IV)

    text = "This is a test".encode()

    ciphertext = aes.encrypt(text)
    plaintext = aes.decrypt(ciphertext)

    print("This is the ciphertext:", ciphertext)
    print("This is the plaintext:", plaintext.decode())

## Setup custom keys:

    from pycryptosimple_aes import *

    key = "This is a key".encode()
    iv = "This is an IV".encode()
    salt = "This is a salt".encode()

    # The hash option will hash the key with the sha256 algorithm
    # and the IV with the md5 algorithm with the salt to
    # prevent brute force attacks 

    aes = simpleAES(key, iv, hash=True, salt=salt)

    text = "This is a text".encode()

    ciphertext = aes.encrypt(text)
    plaintext = aes.decrypt(ciphertext)

    print("ciphertext:", ciphertext)
    print("plaintext:", plaintext.decode())

---

### Store the key to a file:

    from pycryptosimple_aes import *

    key = keyGenerator()
    IV = ivGenerator()

    aes = simpleAES(key, IV)

    path = "key.key"

    aes.extractKey(path)

### Store the key to an encrypted file:

    from pycryptosimple_aes import *
    
    key = keyGenerator()
    iv = ivGenerator()

    aes = simpleAES(key, iv)

    key2 = "abcde".encode()
    iv2 = "12345".encode()
    salt = "qwerty".encode()

    aes2 = simpleAES(key, iv , hash=True, salt=salt)

    path="encryptedKey.key"

    #It will encrypt the file with the 'aes2' object.

    aes.extractEncryptedKey(aes2, path)




### Load the key from file:

    from pycryptosimple_aes import *

    path = "key.key"

    data = loadKeyFromFile(path)

    key = data[0]
    IV = data[1]

    # When you load a key from file do not set the 
    # hash value to True or use the salt option,
    # because in the file are stored the hashed values and not
    # the original keywords.
    
    aes = simpleAES(key, IV)

### Load the key from encrypted file:

    key = "abcde".encode()
    iv = "12345".encode()
    salt = "qwerty".encode()

    aes = simpleAES(key, iv, hash=True, salt=salt)

    path="encryptedKey.key"

    data = loadKeyFromEncryptedFile(aes, path)

    key = data[0]
    iv = data[1]

    aes = simpleAES(key, iv)
