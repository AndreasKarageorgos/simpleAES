# Simple AES

An easy way to use the aes CBC mode of pycryptodome.
To use this library just drag and drop the 'simpleAES.py' file into your work bench and import it to your program.

## Dependencies

    pip install pycryptodome

# Code examples

## Automated key generation:

    from simpleAES import *

    key = keyGenerator()
    IV = ivGenerator()

    aes = simpleAES(key, IV)

    text = "This is a test".encode()

    ciphertext = aes.encrypt(text)
    plaintext = aes.decrypt(ciphertext)

    print("This is the ciphertext:", ciphertext)
    print("This is the plaintext:", plaintext.decode())

## Setup custom keys:

    from simpleAES import *

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

    from simpleAES import *

    key = keyGenerator()
    IV = ivGenerator()

    aes = simpleAES(key, IV)

    path = "key.key"

    aes.extractKey(path)


### Load the key from file:

    from simpleAES import *

    path = "key.key"

    data = loadKeyFromFile(path)

    key = data[0]
    IV = data[1]

    # When you load a key from file do not set the 
    # hash value to True or use the salt option,
    # because in the file are stored the hashed values and not
    # the original keywords.
    
    aes = simpleAES(key, IV)