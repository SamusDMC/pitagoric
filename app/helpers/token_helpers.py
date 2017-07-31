# -*- coding: utf-8 -*-

from flask import current_app, redirect, url_for, Response
from jwt import decode

from . import res_helpers


def invalid_token_res(error):
    """Response for invalid tokens"""
    headers = res_helpers.content_type('json')

    return Response(error, 401, headers)


def remove_token_expired():
    """Function for remove the cookie with token expired"""
    redirect_to_login = redirect(url_for('login'))
    response = current_app.make_response(redirect_to_login)
    response.set_cookie('token', '', expires=0)

    return response


def decode_token(token):
    """Function for decode token of authentication"""
    secret_key = 'dEwq43FalLñpq12Nb!XqKio#'
    algorithms = ['HS256']

    return decode(token, secret_key, algorithms=algorithms)
