from os import path, getenv

BASE_DIR = path.abspath(path.dirname(__file__))

# FLask-via
VIA_ROUTES_MODULE = 'app.routes'

# Flask-SQLAlchemy
if getenv('FAKE') != 'persist':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(path.join(BASE_DIR, 'app.db'))
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(path.join(BASE_DIR, 'tests/app.test.db'))

SQLALCHEMY_TRACK_MODIFICATIONS = True

# Flask-babel
BABEL_DEFAULT_LOCALE = 'es'
