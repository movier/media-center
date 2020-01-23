from datetime import datetime
from flask import Flask, request, g
from flask_restful import Resource, Api, fields, reqparse, abort, marshal
# from database import db_session, db_session2
from manage import Video, Shot
from flask_cors import CORS
from sqlalchemy import desc
from os import listdir
from os.path import isfile, join, splitext, getmtime
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from math import floor

app = Flask(__name__)
CORS(app)
api = Api(app)

cast_fields = {
  'id': fields.Integer,
  'name': fields.String,
}
resource_fields = {
  'id': fields.Integer,
  'title': fields.String,
  'uri': fields.String,
  'poster_uri': fields.String,
  'mtime': fields.DateTime(dt_format='iso8601'),
  'cast': fields.List(fields.Nested(cast_fields)),
}

def is_kids_video(url):
  if not url:
    return False
  x = url.split(":")
  return len(x) > 2 and x[2].startswith("9001/")

def get_db_session():
  if is_kids_video(request.referrer):
    engine2 = create_engine('sqlite:////mnt/sda4/jffs/my-video-app/flask/kids.db', convert_unicode=True)
    db_session2 = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine2))
    return db_session2
  engine = create_engine('sqlite:////mnt/sda4/jffs/my-video-app/flask/test.db', convert_unicode=True)
  db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
  return db_session

def get_static_path():
  if is_kids_video(request.referrer):
    return "/mnt/sda4/data/kids"
  return "/mnt/sda4/data/AI"

def traverse_dir(base_path):
  for f in listdir(base_path):
    path = join(base_path, f)
    if isfile(path):
      title, ext = splitext(f)
      if ext == ".mp4" and not f.startswith("._"):
        title = "".join(title)
        uri = path[len(g.path):]
        root, ext1 = splitext(uri)
        poster_uri = "".join(root) + ".jpg"
        mtimestamp = getmtime(path)
        mdatetime = datetime.fromtimestamp(mtimestamp)
        query_existing_video = g.db.query(Video).filter(Video.title == title).count()
        if query_existing_video == 0:
          v = Video(title=title, uri=uri,
            poster_uri=poster_uri, mtime=mdatetime)
          g.db.add(v)
    else:
      traverse_dir(path)

def check_last_shot_date():
  last_shot = g.db.query(Shot).order_by(Shot.id.desc()).first()
  if not last_shot: return
  now = datetime.now()
  return now - last_shot.created_date

class HelloWorld(Resource):
  def get(self):
    difference = check_last_shot_date()
    if difference and difference.days < 7:
      remaining_seconds = 7 * 24 * 60 * 60 - floor(difference.total_seconds())
      return {
        'has_error': True,
        'error_code': 403,
        'error_message': 'It is less than 7 days since last time you shot. ',
        'data': {'remaining_seconds': remaining_seconds}
      }
    print(request.referrer)
    parser = reqparse.RequestParser()
    parser.add_argument('is_check', type=bool)
    args = parser.parse_args()
    if args['is_check']:
      traverse_dir(g.path)
      g.db.commit()
    result = g.db.query(Video).order_by(desc(Video.mtime)).all()
    return marshal(result, resource_fields), 200

def abort_if_video_doesnt_exist(video_id):
  video = g.db.query(Video).get(video_id)
  if not video:
    abort(404, message="Video {} doesn't exist".format(video_id))
  return video

def remove_file(path):
  if os.path.exists(path):
    os.remove(path)
  else:
    print('The file does not exist')

class VideoController(Resource):
  def delete(self, video_id):
    video = abort_if_video_doesnt_exist(video_id)
    poster_file_path = g.path + video.poster_uri
    remove_file(poster_file_path)
    video_file_path = g.path + video.uri
    remove_file(video_file_path)
    g.db.delete(video)
    g.db.commit()
    return '', 204

class ShotList(Resource):
  def post(self):
    g.db.add(Shot())
    g.db.commit()
    return '', 201

api.add_resource(VideoController, '/videos/<video_id>')
api.add_resource(ShotList, '/shots')
api.add_resource(HelloWorld, '/')

@app.before_request
def open_db_session():
  print("before request", request.referrer)
  if 'db' not in g:
    g.db = get_db_session()
  if 'path' not in g:
    g.path = get_static_path()

@app.teardown_appcontext
def shutdown_session(exception=None):
  print("shut down session")
  db = g.pop('db', None)
  if db is not None:
    db.remove()
