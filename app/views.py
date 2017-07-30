# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from math import pi
import json

from flask import render_template, url_for, request, redirect, Response, jsonify, current_app
from flask.views import MethodView
from flask_babel import get_locale
import jwt

from models import User, db
from decorators import auth_required
from helpers import access_denied_res

login_errors_dict = {
    'error': 'login',
    'username': False,
}


# Functional view for display the index page.
def index():
    return render_template('index.jinja', locale=get_locale())


# Class view for sign-up at the site.
class SignUp(MethodView):

    def get(self):
        return render_template('auth/signup.jinja')

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
        return render_template('auth/login.jinja')

    def post(self):
        secret_key = 'dEwq43FalLñpq12Nb!'
        auth = request.authorization
        username = auth.username
        password = auth.password
        user = db.session.query(User).filter_by(username=username).first()

        if user is None:
            return access_denied_res(json.dumps(login_errors_dict))
        else:
            login_errors_dict['username'] = True

            if password == user.password:
                response = current_app.make_response('')
                token = jwt.encode({
                    'id': str(user.id),
                    'exp': datetime.utcnow() + timedelta(minutes=5)
                }, secret_key, algorithm='HS256')
                response.set_cookie('token', value=token)

                return response
            else:
                return access_denied_res(json.dumps(login_errors_dict))
