import hashlib

"""petit essais sur les hash"""
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
bob="dimitri"
#il faut encoder le string avant de le hasher.
di=bob.encode()
print(di)
print(hashlib.md5(di))
a=hashlib.md5(di)
print(a)
