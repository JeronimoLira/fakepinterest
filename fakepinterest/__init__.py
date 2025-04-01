import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
if os.getenv("DEBUG") == 0:
    link_BD = os.getenv("DATABASE_URL")
else:
    link_BD = "sqlite:///comunidade.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = link_BD

app.config["SECRET_KEY"] = "dd6c6aecba9edab6274cb50e47bcdf26"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


from fakepinterest import routes
