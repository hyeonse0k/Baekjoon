import hashlib

s = input()
encoded_s = s.encode()
print(hashlib.sha256(encoded_s).hexdigest())