
import hashlib


def encryption(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()
