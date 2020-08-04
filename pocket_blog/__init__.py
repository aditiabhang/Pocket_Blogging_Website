import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from pocket_blog.config import Config, DevelopmentConfig

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    # Working command:
    # app.config.from_object(DevelopmentConfig)

    app.config.from_object(os.environ['APP_SETTINGS'])
    # app.config.from_envvar("APP_SETTINGS")

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from pocket_blog.users.routes import users
    from pocket_blog.posts.routes import posts
    from pocket_blog.main.routes import main
    from pocket_blog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
