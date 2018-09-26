import os
import sys
import logging

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail

from zadacha.config import config

db = SQLAlchemy()
migrate = Migrate()
security = Security()
mail = Mail()

def create_app(config_name):
    """Flask application factory.

    :param config_name: Flask configuration

    :type config_name: zadacha.config class

    :returns: a Flask application.
    """
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    app = Flask('zadacha')
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from zadacha.models.user import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    from zadacha.core.views import core
    app.register_blueprint(core)

    from zadacha.auth.views import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app