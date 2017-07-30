# Run cool stuff of mathematics.
from os import getenv

from app import create_app


PORT = getenv('PORT') or '8080'
DEBUG = getenv('DEBUG')
DEV = getenv('DEV')
FAKE = getenv('FAKE')

CONFIG_FILE = '../config.py'
HOST = '127.0.0.1'

app = create_app(CONFIG_FILE, bool(FAKE))

app.run(host=HOST, port=int(PORT), debug=bool(DEBUG))
