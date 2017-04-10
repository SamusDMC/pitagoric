# Run cool stuff of mathematics.
from os import getenv

from app import create_app

PORT = getenv('PORT') or '8080'
DEBUG = getenv('DEBUG')
HOST = '127.0.0.1'
app = create_app('../config.py')
app.run(host=HOST, port=int(PORT), debug=bool(DEBUG))
