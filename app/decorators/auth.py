from functools import wraps
import json

from flask import request, redirect, url_for
import jwt

from ..models import db, User
from ..helpers.token_helpers import invalid_token_res, remove_token_expired, decode_token


def login_required_ajax(func):
    """
    Decorator for verify the token of authentication,
    and response with request body. This route is for ajax request.
    """
    token_errors_dict = {
        'error': 'token',
        'exist': True,
        'expired': False,
    }

    @wraps(func)
    def new_function(*args, **kargs):
        if 'token' in request.cookies:
            token = request.cookies.get('token')

            try:
                token_decoded = decode_token(token)
            except jwt.ExpiredSignatureError:
                token_errors_dict['expired'] = True

                return invalid_token_res(json.dumps(token_errors_dict))

            user_id = token_decoded['id']
            user = db.session.query(User).filter_by(id=user_id).first()

            if user is not None:
                kargs['current_user'] = user

                return func(*args, **kargs)
            else:
                return invalid_token_res(json.dumps(token_errors_dict))
        else:
            token_errors_dict['exist'] = False

            return invalid_token_res(json.dumps(token_errors_dict))

    return new_function


def login_required(func):
    """Decorator for verify the access token"""
    @wraps(func)
    def new_function(*args, **kargs):
        if 'token' in request.cookies:
            token = request.cookies.get('token')

            try:
                token_decoded = decode_token(token)
            except jwt.ExpiredSignatureError:
                return remove_token_expired()

            user_id = token_decoded['id']

            if db.session.query(User).filter_by(id=user_id).first() is None:
                return redirect(url_for('login'))

            return func(*args, **kargs)
        else:
            return redirect(url_for('login'))

    return new_function
