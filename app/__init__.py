from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://marcos:getaways@localhost/jworld'

app.config['SECRET_KEY'] = '944d51c0258f07f940b031b2'
login_manager = LoginManager(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from app import routes

