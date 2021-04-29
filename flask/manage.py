import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/sda4/jffs/my-video-app/flask/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/sda4/jffs/my-video-app/flask/kids.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

media_people_table = db.Table('media_people', db.Model.metadata,
  db.Column('media_id', db.Integer, db.ForeignKey('media.id')),
  db.Column('people_id', db.Integer, db.ForeignKey('people.id'))
)

class Media(db.Model):
  __tablename__ = 'media'
  id = db.Column(db.Integer, primary_key=True, index=True)
  title = db.Column(db.String, index=True)
  uri = db.Column(db.String)
  poster_uri = db.Column(db.String)
  created_at = db.Column(db.DateTime, index=True)
  media_type = db.Column(db.Integer) # 1 for video, 2 for photo, 3 for live_photo
  size = db.Column(db.Integer)
  datetime = db.Column(db.DateTime, index=True)
  duration = db.Column(db.Float)
  filename = db.Column(db.String)
  people = db.relationship(
    'People',
    secondary=media_people_table,
    back_populates="media")

class People(db.Model):
  __tablename__ = 'people'
  id = db.Column(db.Integer, primary_key=True, index=True)
  name = db.Column(db.String, index=True, unique=True)
  media = db.relationship(
    'Media',
    secondary=media_people_table,
    back_populates="people")

class Shot(db.Model):
  __tablename__ = 'shots'

  id = db.Column(db.Integer, primary_key=True, index=True)
  created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

if __name__ == '__main__':
    manager.run()