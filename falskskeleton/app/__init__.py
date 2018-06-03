from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_pymongo import PyMongo
from .main import main as main_blueprint
from config import config




bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
mongo = PyMongo()


def create_app(config_name):

    # App related creation
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    app.register_blueprint(main_blueprint)

    # make all config available
    config[config_name].init_app(app)

    # init all auxiliary plugins
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    mongo.init_app(app)

    # attach route and custom error page here.

    return app


