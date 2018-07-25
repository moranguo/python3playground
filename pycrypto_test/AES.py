from Crypto.Cipher import AES
from Crypto.Random import random

# 使用pycrypto‎dome库
# TypeError: Object type <class 'str'> cannot be passed to C code
# 经过Debug发现，是因为传入参数的参数类型存在问题，需要更换为 bytearray

obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
message = b"The answer is no"
ciphertext = obj.encrypt(message)
print(ciphertext)

obj2 = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
plaintxt = obj2.decrypt(ciphertext)
print(plaintxt)

print(random.choice(['dogs', 'cats', 'bears']))