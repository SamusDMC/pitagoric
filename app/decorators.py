from functools import wraps
from flask import render_template, url_for, redirect, session


def check_session(func):
    @wraps(func)
    def new_function(*args, **kargs):
        if 'username' in session:
            user = session['username']
            return redirect(url_for('user.profile', user=user))
        else:
            return func(*args, **kargs)

    return new_function
