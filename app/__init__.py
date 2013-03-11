import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
loginmanager = LoginManager()
loginmanager.init_app(app)
loginmanager.login_view = 'login'
# oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models

