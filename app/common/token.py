# -*- coding: utf-8 -*-

import os
import time
import base64  # base41 可逆

secret_key = os.urandom(24)

'''生成token
'''
def generate_token(username, role):
    '''合法、过期等
    '''
    #base64.b64encode()
    #base64.b64decode()
    expire_time = int(time.time() + 60 * 60 * 12)
    tokenTmp = "%s|%s|%s|%s" % (secret_key, username, role, expire_time)
    return base64.b64encode(tokenTmp) 


'''验证token
'''
def varify_token(token):
    tokenTmp = base64.b64decode(token).split("|")
    if len(tokenTmp) == 4:
        secret_key, username, role, expire_time = tokenTmp
        if int(expire_time) > time.time():
            return (username, role), True
        else:
            return 'token expire', False
    else:
        return 'wrong key', False




if __name__ == '__main__':
    token = generate_token('monkey', 'admin')
    print token
    print varify_token(token)
