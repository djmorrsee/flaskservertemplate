from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db/data.db'
db = SQLAlchemy(app)

class TableDef(db.Model):
    _id = db.Column(db.Integer, primary_key = True, unique=True)

    #Custom Properties
    name = db.Column(db.String)
