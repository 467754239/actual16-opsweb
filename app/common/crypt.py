
import hashlib


def encryption(data_string):
    m = hashlib.md5()
    m.update(data_string.encode('utf-8'))
    return m.hexdigest()
