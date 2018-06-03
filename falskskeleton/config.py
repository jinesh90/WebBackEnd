import os
basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)


class Config:
    """
    Base config for flask app
    """
    SECRET_KEY = "jinesh",
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <jinesh90@gmail.com>'
    FLASKY_ADMIN = 'jinesh'
    MONGO_DBNAME = 'user'
    MONGO_URI = 'mongodb://localhost:27017/user'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jinesh90@gmail.com'
    MAIL_PASSWORD = 'password'


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass

config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}

