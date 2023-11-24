'''
Created on Nov 22, 2023

@author: NKarhe
'''
import logging
import sys
import os
import urllib
import json

from flask_sqlalchemy import SQLAlchemy

app = None
debug = os.getenv("DEBUG") is not None
db = SQLAlchemy()
applogger = logging.getLogger("speechtotext.api")

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
    db_uri = "sqlite:///" + os.getcwd() + "\\openapi_server\\dbmodels\\cvscanner.db"
    applogger.info("Initializing API")
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
    #db.create_all()

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