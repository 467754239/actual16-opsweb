# -*- coding: utf-8 -*-

import os
import time
import base64  # base41 可逆


from itsdangerous import BadTimeSignature, BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

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


'''
http://pythonhosted.org/itsdangerous/
http://itsdangerous.readthedocs.io/en/latest/
http://www.jb51.net/article/110254.htm
'''
class Token(object):

    def __init__(self, secret_key, max_token_age):
        self.secret_key = secret_key
        self.max_token_age = max_token_age  # second
        self.token_generator = Serializer(self.secret_key, expires_in=self.max_token_age)
        
    def generate_auth_token(self, data):
        return self.token_generator.dumps({ "token" : data })
    
    def verify_token(self, token):
        try:
            user_auth = self.token_generator.loads(token)
        except SignatureExpired as e:
            return "签名已过期.", False
        except BadSignature as e:
            return "错误的签名.", False
        except BadTimeSignature as e:
            return "错误的时间签名.", False
        except Exception as e:
            return "Unknow exception.", False
        else:
            return user_auth, True


if __name__ == '__main__':
    pass
