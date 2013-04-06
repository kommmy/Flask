import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
loginmanager = LoginManager()
loginmanager.init_app(app)
loginmanager.login_view = 'login'
loginmanager.refresh_view = "reauth"
loginmanager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page.")


from app import views, models

