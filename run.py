#!/usr/bin/env python

from os import getenv

from app import create_app


PORT = getenv('PORT') or '8080'
DEBUG = getenv('DEBUG')
DEV = getenv('DEV')

app = create_app()

app.run(host='127.0.0.1', port=int(PORT), debug=bool(DEBUG))
