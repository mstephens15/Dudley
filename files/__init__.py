from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from files.config import Config

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
mail = Mail()

#Working with the admin page!
from files.models import User, Controller, MyAdmin

admin = Admin(index_view=MyAdmin())
admin.add_view(Controller(User, db.session))

#change the alert if it asks people to sign in first
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    admin.init_app(app)

#The last part (users, posts, main, errors etc.) is the first line, that equals the blueprint
    from files.users.routes import users
    from files.posts.routes import posts
    from files.main.routes import main
    from files.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app