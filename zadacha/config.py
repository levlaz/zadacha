import os


class Config:
    """Base Config class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
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


config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,

        'default': DevelopmentConfig
}