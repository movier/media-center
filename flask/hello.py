from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from database import db_session
from models import Video
from flask_cors import CORS
from sqlalchemy import desc
from os import listdir
from os.path import isfile, join, splitext, getmtime
from datetime import datetime

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

mypath = "/mnt/sda4/data/AI"

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
          db_session.add(v)
    else:
      traverse_dir(path)

class HelloWorld(Resource):
  @marshal_with(resource_fields)
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('is_check', type=bool)
    args = parser.parse_args()
    if args['is_check']:
      traverse_dir(mypath)
      db_session.commit()
    return Video.query.order_by(desc(Video.mtime)).all()

api.add_resource(HelloWorld, '/')

@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()
