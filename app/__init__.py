from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = "./app/static/profilepictures"

app = Flask(__name__)
app.config['SECRET_KEY'] = "password123"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://avaughn:password123@localhost/users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views