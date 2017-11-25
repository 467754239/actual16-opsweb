

from flask import session
from flask import redirect
from functools import wraps

from .users import get_password_from_username

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not session.get('sign', None):
            return redirect('/login')
        return func(*args, **kwargs)

    return wrapper


def authentication(username, password):

    tuple_password = get_password_from_username(username)
    if not tuple_password:
        return 'Username: %s not register.' % username, False

    if password != tuple_password[0][0]:
        return 'Username: %s, bad password' % username, False 

    return None, True
