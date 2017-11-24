
import md5


def encryption(data):
    return md5.md5(data).hexdigest()
