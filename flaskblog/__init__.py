from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'c637300bb59271eb97d968c59086b5b0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes