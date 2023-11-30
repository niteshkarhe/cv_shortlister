'''
Created on Nov 22, 2023

@author: NKarhe
'''
import logging
import sys
import os
import urllib
import json
import sqlite3
from sqlite3 import Error

from flask_sqlalchemy import SQLAlchemy

app = None
debug = os.getenv("DEBUG") is not None
db = SQLAlchemy()
applogger = logging.getLogger("cv_shortlister.api")

def get_logger():
    global applogger
    return applogger

def get_config():
    global app
    return app.config

def init_app(application):
    # initialize app
    global app
    app = application

    # initialize Loggers
    init_logging()

    global applogger

    #db_uri = "sqlite:///" + os.getcwd() + "\\openapi_server\\database\\cvscanner.db"
    db_uri = "sqlite:///" + "cvscanner.db"

    #connection = sqlite3.connect('cvscanner.db')
    #cursor = connection.cursor()
    #create_table = "CREATE TABLE users (id integer, email text, name text, role text, question text, answer text, percentage integer, result text, recordingpath text, date text)"
    #create_table = "CREATE TABLE questions (id integer, role text, hr_email text, question text, expected_answer text)"
    #create_table = "CREATE TABLE jobs (id integer, role text, hr_email text)"
    #cursor.execute(create_table)

    applogger.info("Initializing API")
    app.config['Content-Type'] = 'application/json'
    app.config['Access-Control-Allow-Origin'] = ['http://localhost:3000', 'http://localhost:8080']
    app.config['Access-Control-Allow-Methods'] = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
    app.config['Access-Control-Allow-Headers'] = ['Origin', 'Content-Type', 'Accept', 'Authorization', 'X-Request-With']
    app.config['SECRET_KEY'] = 'MySecretKeyNeedsToBeChanged'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_ECHO"] = debug

    # Database Pool size
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_size": 50,
        "pool_recycle": 120,
        "pool_pre_ping": True,
    }

    db.init_app(app)
    with app.app_context():
        db.create_all()

def init_logging():
    global applogger
    global debug

    if debug:
        applogger.setLevel(logging.DEBUG)
    else:
        applogger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        json.dumps(
            {
                "message": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                "severity": "%(levelname)s",
            }
        )
    )

    handler.setFormatter(formatter)
    applogger.addHandler(handler)