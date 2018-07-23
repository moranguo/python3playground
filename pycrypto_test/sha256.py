from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update(b'message')
print(hash.digest())
print(hash.hexdigest())