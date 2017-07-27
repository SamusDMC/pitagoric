# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_via import Via
from models import db
from flask_compress import Compress
from fake_data import create_fake_data

compress = Compress()
via = Via()


def create_app(config_file, fake=False):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.secret_key = 'dEwq43FalLñpq12Nb!'

    # Initializes.
    via.init_app(app)
    db.init_app(app)
    compress.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

        # Creator of fake data.
        if fake:
            create_fake_data(db)
            db.session.commit()

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('error/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error/404.html', title='Page not found'), 404

    return app
