import os
import functools

from datetime import timedelta
#import jwt

from flask import Flask, redirect, request, jsonify, url_for, g, session, render_template, make_response, abort

#import aws_config as awsc


server = Flask(__name__)
# export FLASK_ENV=development or FLASK_ENV=production

server.config['AWS_DEFAULT_REGION'] = awsc.region

# reduce session timeout
server.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=120)
server.config["SECRET_KEY"] = os.urandom(12)



@server.route('/')
def index():    
	return render_template('index.html')





