from functools import wraps
from flask import render_template, url_for, redirect, session
from helpers import session_exists


def check_session(f):
    @wraps(f)
    def new_function(*args, **kargs):
        if session_exists('username'):
            user = session['username']
            return redirect(url_for('user.profile', user=user))
        else:
            return f(*args, **kargs)
    return new_function
