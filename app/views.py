from . import app
from flask import render_template
import math


@app.route('/')
def index():
    return render_template('index.html', pi=math.pi)
