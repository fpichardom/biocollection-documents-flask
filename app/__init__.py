from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__, static_folder='static')
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# Name of the function or endpoint that handles the login
login.login_view = 'login'

# Left these imports in the end to avoid circular imports
from app import routes, models