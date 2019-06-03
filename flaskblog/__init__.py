import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail #using gmail for email handling


app = Flask(__name__)
app.config['SECRET_KEY'] = 'de104ecad906b0ca18ef455a25c32172'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#init encryption for reg/log in
bcrypt = Bcrypt(app)
#login/logout management
login_manager = LoginManager(app)
login_manager.login_view = 'login'
#fix bootstrap class on flash message for login required
login_manager.login_message_category = 'info'
#set up how to send emails -- using GMAIL for email handling
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] =os.environ.get('EMIAL_PASS')
mail = mail(app)


from flaskblog import routes
