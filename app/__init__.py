# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_via import Via
from flask_compress import Compress
from flask_babel import Babel

from fake_data import create_fake_data
from models import db

compress = Compress()
via = Via()
babel = Babel()


def create_app():
    """
    Factory app.
    """

    # Create the app.
    app = Flask(__name__)

    # File configuration from a file.
    app.config.from_pyfile('../config.py')

    # Initializes.
    via.init_app(app)
    db.init_app(app)
    compress.init_app(app)
    babel.init_app(app)

    with app.app_context():
        db.create_all()

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('error/403.jinja', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error/404.jinja', title='Page not found'), 404

    return app
