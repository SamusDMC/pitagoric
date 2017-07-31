# -*- coding: utf-8 -*-

from functools import wraps
import json

from flask import request
import jwt

from models import db, User
from helpers import invalid_token_res

token_errors_dict = {
    'error': 'token',
    'exist': True,
    'expired': False,
}


def auth_required(func):
    @wraps(func)
    def new_function(*args, **kargs):
        if 'token' in request.cookies:
            token = request.cookies.get('token')

            try:
                token_decoded = jwt.decode(token, 'dEwq43FalLñpq12Nb!XqKio#', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                token_errors_dict['expired'] = True

                return invalid_token_res(json.dumps(token_errors_dict))

            user_id = token_decoded['id']
            user = db.session.query(User).filter_by(id=user_id).first()

            if user is not None:
                kargs['user_session'] = user

                return func(*args, **kargs)
            else:
                return invalid_token_res(json.dumps(token_errors_dict))
        else:
            token_errors_dict['exist'] = False

            return invalid_token_res(json.dumps(token_errors_dict))

    return new_function
