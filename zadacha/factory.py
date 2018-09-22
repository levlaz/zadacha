from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from zadacha.config import config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    """Flask application factory.

    :param config_name: Flask configuration

    :type config_name: zadacha.config class

    :returns: a Flask application.
    """
    app = Flask('zadacha')
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    migrate.init_app(app, db)

    from zadacha.core.views import core
    app.register_blueprint(core)

    from zadacha.auth.views import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app