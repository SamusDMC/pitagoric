# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.via import Via
from models import db


def create_app(config_file):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.secret_key = 'dEwq43FalLñpq12Nb!'
    via = Via()
    via.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('error/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error/404.html', title='Page not found'), 404

    return app
