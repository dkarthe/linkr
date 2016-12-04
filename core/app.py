import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

template_directory = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'frontend/templates'
)
static_directory = 'frontend/static'

app = Flask(__name__, template_folder=template_directory, static_folder=static_directory)
app.config.from_object('config.flask_config')


def init_db():
    """
    Initialize the SQLAlchemy database object.

    :return: A SQLAlchemy instance used universally for database operations.
    """
    return SQLAlchemy(app, session_options={
        'expire_on_commit': False,
    })


def init_login_manager():
    """
    Initialize the login manager.

    :return: A LoginManager instance used universally for flask-login loaders.
    """
    login_manager = LoginManager()
    login_manager.init_app(app)
    return login_manager