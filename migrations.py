from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, './app.db')
session_options = {'autocommit': False, 'autoflush': False}
db = SQLAlchemy(app, session_options=session_options)


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    start_date = db.Column(db.DateTime, unique=False, nullable=False)
    finish_date = db.Column(db.DateTime, unique=False, nullable=False)
    status = db.Column(db.String(80), unique=False, nullable=False)


# db.drop_all()
db.create_all()
for num in range(100):
    log = Log(name='name {}'.format(num), start_date=datetime(2012, 3, 3, 10, 10, 10),
              finish_date=datetime(2012, 3, 3, 10, 10, 10), status='In progress {}'.format(num))
    db.session.add(log)

db.session.flush()
db.session.commit()
