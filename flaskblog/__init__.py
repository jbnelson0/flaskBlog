from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'de104ecad906b0ca18ef455a25c32172'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
#init encryption for reg/log in
bcrypt = Bcrypt(app)

from flaskblog import routes
