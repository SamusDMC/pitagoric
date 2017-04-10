from flask import session


def session_exists(key):
    return key in session
