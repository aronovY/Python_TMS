from flask import Flask
import os
import flask_sqlalchemy
from flask_migrate import Migrate
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'currency.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login = LoginManager(app)
login.login_view = 'login'

db = flask_sqlalchemy.SQLAlchemy(app)

from app import models

migrate = Migrate(app, db)


uri = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

from app import routes
