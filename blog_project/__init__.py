from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

uri = 'mysql+pymysql://root:root1234@localhost'
database = 'blog_database'
engine = create_engine(uri)
engine.execute('CREATE DATABASE IF NOT EXISTS %s;' % database)
engine.execute('USE %s' % database)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = uri + '/' + database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)

from blog_project import routes

