# Run cool stuff of mathematics.
from os import getenv

from app import create_app

config_file = '../config.py'

PORT = getenv('PORT') or '8080'
DEBUG = getenv('DEBUG')
DEV = getenv('DEV')
HOST = '127.0.0.1'

# For development.
if bool(DEV):
    # Create app with fake data.
    app = create_app(config_file, True)
else:
    app = create_app(config_file)

app.run(host=HOST, port=int(PORT), debug=bool(DEBUG))
