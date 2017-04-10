from flask import render_template, url_for, request, redirect, session
from flask.views import MethodView
from models import User, db
from helpers import *
from decorators import check_session

from math import pi


@check_session
def index():
    return render_template('index.html', pi=pi)


class SignUp(MethodView):

    @check_session
    def get(self):
        return render_template('security/signup.html')

    def post(self):
        data = request.form
        username = data['username']
        email = data['email']
        password = data['password']
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))


class LogIn(MethodView):

    @check_session
    def get(self):
        return render_template('security/login.html')

    def post(self):
        data = request.form
        username = data['username']
        password = data['password']
        user = db.session.query(User).filter_by(username=username).first()

        if user is None:
            return render_template('login.html', error_user=True)
        else:
            session['username'] = username
            return redirect(url_for('user.profile', user=username))
