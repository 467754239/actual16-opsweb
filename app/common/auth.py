

from flask import session
from flask import request 
from flask import redirect
from functools import wraps

import requests

from .users import get_password_from_username
from .crypt import encryption

from app import app


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        app.logger.info('>>> auth headers: \n%s' % request.headers)
        app.logger.info('>>> auth cookies: %s' % request.cookies)

        if not session.get('sign', None):
            return redirect('/login')
        return func(*args, **kwargs)

    return wrapper


def authentication(username, password):

    tuple_password = get_password_from_username(username)
    if not tuple_password:
        return 'Username: %s not register.' % username, False

    print tuple_password
    print encryption(password)
    if encryption(password) != tuple_password[0]:
        return 'Username: %s, bad password' % username, False 

    return None, True


def github_auth(username, password):
    '''
    https://developer.github.com/v3/
    '''
    req = requests.get(url='https://api.github.com',auth=(username, password))
    return None, req.ok
