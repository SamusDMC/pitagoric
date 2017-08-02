# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from math import pi
import json

from flask import render_template, url_for, request, redirect, Response, jsonify, current_app
from flask.views import MethodView
from flask_babel import get_locale
import jwt

from models import User, db
from helpers.res_helpers import access_denied_res


def index():
    """
    Functional view for render the index page.
    """

    return render_template('index.jinja', locale=get_locale())


# Class view for sign-up at the site.
class SignUp(MethodView):

    def get(self):
        return render_template('auth/signup.jinja', locale=get_locale())

    def post(self):
        data = request.form
        fullname = data['fullname']
        username = data['username']
        email = data['email']
        password = data['password']
        bio = data['bio']
        user = User(fullname, username, email, password, None, bio)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))


# Class view for log-in at the site.
class LogIn(MethodView):

    def get(self):
        return render_template('auth/login.jinja', locale=get_locale())

    def post(self):
        login_errors_dict = {
            'error': 'login',
            'username': False,
        }
        auth = request.authorization
        username, password = auth.username, auth.password
        user = db.session.query(User).filter_by(username=username).first()

        if user is not None:
            token_dict = {
                'id': str(user.id),
                'exp': datetime.utcnow() + timedelta(minutes=5),
            }

            if password == user.password:
                response = current_app.make_response('')
                token = jwt.encode(token_dict, 'dEwq43FalLñpq12Nb!XqKio#', algorithm='HS256')
                response.set_cookie('token', value=token)

                return response
            else:
                login_errors_dict['username'] = True

        return access_denied_res(json.dumps(login_errors_dict))
