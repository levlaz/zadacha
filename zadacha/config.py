import os
import ldclient

class Config:
    """Base Config class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Security
    SECURITY_URL_PREFIX = "/auth"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = SECRET_KEY
    SECURITY_EMAIL_SENDER = "noreply@zadacha.app"
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_CHANGEABLE = True

    # LaunchDarkly
    ldclient.set_sdk_key(os.environ.get("LD_SDK_KEY"))

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{0}@{1}/{0}'.format(
            'zadacha',
            'localhost')
    MAIL_SUPPRESS_SEND = True

    @staticmethod
    def init_app(app):
        Config.init_app(app)

        with app.app_context():
            from zadacha.factory import db
            from zadacha.models.user import User

            db.init_app(app)


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{0}@{1}/{0}'.format(
            'zadacha',
            'localhost')

    @staticmethod
    def init_app(app):
        Config.init_app(app)

        with app.app_context():
            from zadacha.factory import db
            from zadacha.models.user import User

            db.init_app(app)
            db.create_all()

            from ldclient.config import Config as __config
            ldclient.set_config(__config(offline=True))

class ProductionConfig(Config):
    SECURITY_CONFIRMABLE = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}/{3}'.format(
            os.environ.get('DB_USER'),
            os.environ.get('DB_PASSWORD'),
            "db",
            "zadacha"
    )

config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,

        'default': DevelopmentConfig
}