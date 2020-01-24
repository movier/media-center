import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/sda4/jffs/my-video-app/flask/test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/sda4/jffs/my-video-app/flask/kids.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

video_cast_table = db.Table('video_cast', db.Model.metadata,
  db.Column('video_id', db.Integer, db.ForeignKey('videos.id')),
  db.Column('cast_id', db.Integer, db.ForeignKey('cast.id'))
)

class Video(db.Model):
  __tablename__ = 'videos'
  id = db.Column(db.Integer, primary_key=True, index=True)
  title = db.Column(db.String, index=True)
  uri = db.Column(db.String)
  poster_uri = db.Column(db.String)
  mtime = db.Column(db.DateTime, index=True)
  cast = db.relationship(
    'Cast',
    secondary=video_cast_table,
    back_populates="videos")

class Cast(db.Model):
  __tablename__ = 'cast'
  id = db.Column(db.Integer, primary_key=True, index=True)
  name = db.Column(db.String, index=True, unique=True)
  videos = db.relationship(
    'Video',
    secondary=video_cast_table,
    back_populates="cast")

class Shot(db.Model):
  __tablename__ = 'shots'

  id = db.Column(db.Integer, primary_key=True, index=True)
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

if __name__ == '__main__':
    manager.run()