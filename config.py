from os import path

BASE_DIR = path.abspath(path.dirname(__file__))

# FLask-via
VIA_ROUTES_MODULE = 'app.routes'

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(path.join(BASE_DIR, 'app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask-babel
BABEL_DEFAULT_LOCALE = 'es'
