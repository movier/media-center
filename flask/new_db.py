import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/sda4/jffs/my-video-app/flask/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/sda4/jffs/my-video-app/flask/kids.db'
db = SQLAlchemy(app)

class Video(db.Model):
  __tablename__ = 'videos'
  id = db.Column(db.Integer, primary_key=True, index=True)
  title = db.Column(db.String, index=True)
  uri = db.Column(db.String)
  poster_uri = db.Column(db.String)
  mtime = db.Column(db.DateTime, index=True)

class Shot(db.Model):
  __tablename__ = 'shots'

  id = db.Column(db.Integer, primary_key=True, index=True)
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

db.create_all()
