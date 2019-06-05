from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail #using gmail for email handling
from flaskblog.config import Config #pull config from os config file


db = SQLAlchemy()
#init encryption for reg/log in
bcrypt = Bcrypt()
#login/logout management
login_manager = LoginManager()
login_manager.login_view = 'users.login'
#fix bootstrap class on flash message for login required
login_manager.login_message_category = 'info'
#set up how to send emails -- using GMAIL for email handling

mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
