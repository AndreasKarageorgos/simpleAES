# Simple AES

An easy way to use the aes CBC mode of pycryptodome.
To use this library just drag and drop the 'simpleAES.py' file into your work bench and import it to your program.

## Dependencies

    pip install pycryptodome

## Code example 1

    from simpleAES import *

    key = keyGenerator()
    IV = ivGenerator()

    aes = simpleAES(key, IV)

    text = "This is a test".encode()

    ciphertext = aes.encrypt(text)
    plaintext = aes.decrypt(ciphertext)

    print("This is the ciphertext:", ciphertext)
    print("This is the plaintext:", plaintext.decode())

## Code example 2

    from simpleAES import *

    key = "This is a key".encode()
    iv = "This is an IV".encode()
    salt = "This is a salt".encode()

    aes = simpleAES(key, iv, hash=True, salt=salt)

    text = "This is a text".encode()

    ciphertext = aes.encrypt(text)
    plaintext = aes.decrypt(ciphertext)

    print("ciphertext:", ciphertext)
    print("plaintext:", plaintext.decode())

---

### Store the keys to a file.

    from simpleAES import *

    keyGenerator()
    IV = ivGenerator()

    aes = simpleAES(key, IV)

    path = "~/keys/"
    keyname = "key.key"

    aes.extractKey(path+keyname)


### Load the keys from file.

    from simpleAES import *

    path = "~/keys/"
    keyname = "key.key"

    data = loadKeyFromFile(path+keyname)

    key = data[0]
    IV = data[1]

    # When you load a key from file do not set the 
    # hash value to True or use the salt option.
    # Unless you know what you are doing.
    
    aes = simpleAES(key, IV)