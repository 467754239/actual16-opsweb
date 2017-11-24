

from flask import session
from flask import redirect
from functools import wraps


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        if not session.get('sign', None):
            return redirect('/login')
        return func(*args, **kwargs)

    return wrapper


def authentication(username, password):

    return True
