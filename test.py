import pathlib
import copy

from flask import session, redirect


#from pyathena import connect
import numpy as np
import pandas as pd
import json

import aws_config as awsc

from flask_server import server
import flask


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')









