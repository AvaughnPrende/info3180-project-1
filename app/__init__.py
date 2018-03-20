from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


UPLOAD_FOLDER = "./app/static/profilepictures"

app = Flask(__name__)
app.config['SECRET_KEY'] = "password123"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://hevtqezckdlcxd:1417b62d5bc83dd2b8f4b213d628f2b59bc8a2eb6becdd674867a72ee7154fe9@ec2-174-129-225-9.compute-1.amazonaws.com:5432/debr9fteudhtcs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views