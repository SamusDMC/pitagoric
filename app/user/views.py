from flask import render_template, url_for, redirect, session
from ..helpers import session_exists


def user(user=None):
    if session_exists('username'):
        return render_template('profile.html', user=user)
    else:
        return redirect(url_for('login'))


def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
