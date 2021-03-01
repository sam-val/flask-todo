from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app_package.config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

login = LoginManager(app)
login.login_view = 'login'

from app_package import routes

