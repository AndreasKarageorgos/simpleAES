# Simple AES

An easy way to use the aes CBC mode of pycryptodome.
To use this library just drag and drop the 'simpleAES.py' file into your work bench and import it to your program.

## Dependencies

    pip install pycryptodome

## Code example

    from simpleAES import *

    key = keyGenerator()
    IV = ivGenerator()

    aes = simpleAES(key, IV)

    text = "This is a test".encode()

    ciphertext = aes.encrypt(text)
    plaintext = aes.decrypt(ciphertext)

    print("This is the ciphertext:", ciphertext)
    print("This is the plaintext:", plaintext.decode())