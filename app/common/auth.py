

from flask import session
from flask import request 
from flask import redirect
from flask import jsonify 
from functools import wraps

import requests

from .users import get_password_from_username
from .users import validate_uid_exists 
from .crypt import encryption

from app import app


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        #app.logger.info('>>> auth headers: \n%s' % request.headers)
        #app.logger.info('>>> auth cookies: %s' % request.cookies)

        if not session.get('sign', None):
            return redirect('/login')
        return func(*args, **kwargs)

    return wrapper

def verify_token(func):

    @wraps(func)
    def decorated(*args, **kwargs):
        #token = request.args.get('token', None)
        token = request.form.get('token', None)
        if not token:
            return jsonify({ 'token' : 'token is required.' })

        token_info, ok = app.config['token'].verify_token(token)
        if not ok:
            return jsonify({ 'token' : token_info })
        
        uid = token_info['token']
        _, uid_ok = validate_uid_exists(uid)
        if not uid_ok:
            return jsonify({ 'token' : 'invalid token.' }) 
        return func(*args, **kwargs)

    return decorated


def authentication(username, password):

    tuple_password = get_password_from_username(username)
    if not tuple_password:
        return 'Username: %s not register.' % username, False

    if encryption(password) != tuple_password[0]:
        return 'Username: %s, bad password.' % username, False 

    return None, True


def github_auth(username, password):
    '''
    https://developer.github.com/v3/
    '''
    req = requests.get(url='https://api.github.com', auth=(username, password))
    return None, req.ok

