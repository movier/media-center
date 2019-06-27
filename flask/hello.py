from flask import Flask, request, g
from flask_restful import Resource, Api, fields, marshal_with, reqparse
# from database import db_session, db_session2
from models import Video
from flask_cors import CORS
from sqlalchemy import desc
from os import listdir
from os.path import isfile, join, splitext, getmtime
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
CORS(app)
api = Api(app)

resource_fields = {
  'id': fields.Integer,
  'title': fields.String,
  'uri': fields.String,
  'poster_uri': fields.String,
  'mtime': fields.DateTime(dt_format='iso8601')
}

mypath = "/mnt/sda4/data/AI" # Todo: should be dynamic

def get_db_session():
  if request.referrer == 'http://localhost:81/':
    print("Hello world")
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

# db_session = get_db_session()

def traverse_dir(base_path):
  for f in listdir(base_path):
    path = join(base_path, f)
    if isfile(path):
      title, ext = splitext(f)
      if ext == ".mp4" and not f.startswith("._"):
        title = "".join(title)
        uri = path[len(mypath):]
        root, ext1 = splitext(uri)
        poster_uri = "".join(root) + ".jpg"
        mtimestamp = getmtime(path)
        mdatetime = datetime.fromtimestamp(mtimestamp)
        query_existing_video = Video.query.filter(Video.title == title).count()
        if query_existing_video == 0:
          v = Video(title=title, uri=uri,
            poster_uri=poster_uri, mtime=mdatetime)
          # db_session.add(v)
    else:
      traverse_dir(path)

class HelloWorld(Resource):
  @marshal_with(resource_fields)
  def get(self):
    print(request.referrer)
    # db_session = get_db_session()
    parser = reqparse.RequestParser()
    parser.add_argument('is_check', type=bool)
    args = parser.parse_args()
    if args['is_check']:
      traverse_dir(mypath)
      # db_session.commit()
    return g.db.query(Video).order_by(desc(Video.mtime)).all()

api.add_resource(HelloWorld, '/')

@app.before_request
def open_db_session():
  print("before request", request.referrer)
  if 'db' not in g:
    g.db = get_db_session()

@app.teardown_appcontext
def shutdown_session(exception=None):
  print("shut down session")
  db = g.pop('db', None)
  if db is not None:
    db.remove()
