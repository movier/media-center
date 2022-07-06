import os, shutil, subprocess
from datetime import datetime
from flask import Flask, request, g, flash, redirect
from flask_restful import Resource, Api, fields, reqparse, abort, marshal
# from database import db_session, db_session2
from manage import Media, Shot, People, AndroidRelease
from flask_cors import CORS
from sqlalchemy import desc
from os import listdir
from os.path import isfile, join, splitext, getmtime, getsize
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from math import floor
from update_duration_and_datetime import get_datetime, get_duration
from traverse_dir import fini
from werkzeug.utils import secure_filename
from utils import generate_thumbnail, get_media_type, get_image_metadata, get_media_dimensions

UPLOAD_FOLDER = '/mnt/sda4/data/AI'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 * 1024 # 1GB
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

CORS(app)
api = Api(app)

cast_fields = {
  'id': fields.Integer,
  'name': fields.String,
}
resource_fields = {
  'id': fields.Integer,
  'size': fields.Integer,
  'title': fields.String,
  'uri': fields.String,
  'poster_uri': fields.String,
  'created_at': fields.DateTime(dt_format='iso8601'),
  'people': fields.List(fields.Nested(cast_fields)),
  'datetime': fields.DateTime(dt_format='iso8601'),
  'duration': fields.Float,
  'media_type': fields.Integer,
  'width': fields.Integer,
  'height': fields.Integer,
}
cast_fields_res = {
  'id': fields.Integer,
  'name': fields.String,
  'media': fields.List(fields.Nested(resource_fields))
}
android_release_fields_res = {
  'id': fields.Integer,
  'version_name': fields.String,
  'version_code': fields.Integer,
  'download_url': fields.String,
  'created_at': fields.DateTime(dt_format='iso8601'),
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

def check_media_exist(filename):
  query_existing_video = g.db.query(Media).filter(Media.filename == filename).count()
  if query_existing_video == 0:
    return False
  return True

# Test
# def traverse_dir(base_path):
#   for f in listdir(base_path):
#     path = join(base_path, f)
#     if isfile(path):
#       title, ext = splitext(f)
#       if not f.startswith("._"):
#         title = "".join(title)
#         # uri = path[len(g.path):]
#         root, ext1 = splitext(path)
#         poster_uri = "".join(root) + ".jpg"
#         mtimestamp = getmtime(path)
#         mdatetime = datetime.fromtimestamp(mtimestamp)
#         file_size = os.path.getsize(path)
#         query_existing_video = g.db.query(Media).filter(Media.title == title).count()
#         if query_existing_video == 0:
#           duration = get_duration(path)
          
#           creation_datetime = get_datetime(path)
#           media_datetime = None
#           if creation_datetime:
#             media_datetime = datetime.strptime(creation_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')

#           v = Media(
#             title=title,
#             uri=path,
#             poster_uri=poster_uri,
#             created_at=mdatetime,
#             media_type=1,
#             size=file_size,
#             duration=duration,
#             datetime=media_datetime,
#           )
#           g.db.add(v)
#     else:
#       traverse_dir(path)

# 遍历目录查找是否有其他文件
def traverse_dir_for_other_media(dir, file_path):
  for f in listdir(dir):
    path = join(dir, f)
    if isfile(path) and path != file_path:
      # query_media = g.db.query(Media).filter(Media.uri == path or Media.poster_uri == path).all()
      # for m in query_media:
      #   if m.id != media_id:
        return True
    elif path == file_path:
      continue
    else:
      return traverse_dir_for_other_media(path, file_path)

class HelloWorld(Resource):
  def get(self):
    print(request.referrer)
    parser = reqparse.RequestParser()
    parser.add_argument('is_check', type=bool)
    args = parser.parse_args()
    if args['is_check']:
      fini(g.path, g.db, True)
    result = g.db.query(Media).order_by(desc(Media.created_at)).all()
    return marshal(result, resource_fields), 200

def abort_if_video_doesnt_exist(media_id):
  media = g.db.query(Media).get(media_id)
  if not media:
    abort(404, message="Media {} doesn't exist".format(media_id))
  return media

def remove_file(path):
  if os.path.exists(path):
    os.remove(path)
  else:
    print('The file does not exist')

class MediaController(Resource):
  def get(self, media_id):
    media = abort_if_video_doesnt_exist(media_id)
    return marshal(media, resource_fields), 200

  def delete(self, media_id):
    media = abort_if_video_doesnt_exist(media_id)

    remove_file(media.poster_uri)
    remove_file(media.uri)

    g.db.delete(media)
    g.db.commit()

    media_dir = os.path.dirname(media.uri)
    if os.path.exists(media_dir):
      if_other_media_in_dir = traverse_dir_for_other_media(media_dir, media.uri)

      if not if_other_media_in_dir:
        if media_dir != get_static_path():
          shutil.rmtree(media_dir)

    return '', 204
  
  def put(self, media_id):
    parser = reqparse.RequestParser()
    parser.add_argument('cast_name')
    args = parser.parse_args()
    cast_name = args['cast_name']
    query_cast = g.db.query(People).filter_by(name=cast_name)

    if query_cast.count() > 0:
      c = query_cast.first()
    else:
      c = People(name=cast_name)

    v = g.db.query(Media).get(media_id)
    v.people.append(c)
    g.db.add(v)
    g.db.commit()
    return True, 200

class ShotList(Resource):
  def post(self):
    g.db.add(Shot())
    g.db.commit()
    return '', 201

class CastController(Resource):
  def get(self):
    result = g.db.query(People).all()
    return marshal(result, cast_fields_res), 200

class AndroidReleaseController(Resource):
  def get(self):
    result = g.db.query(AndroidRelease).order_by(AndroidRelease.version_code.desc()).first()
    return marshal(result, android_release_fields_res), 200
  # def post(self):
  #   parser = reqparse.RequestParser()
  #   parser.add_argument('version_name')
  #   parser.add_argument('version_code')
  #   args = parser.parse_args()
  #   version_name = args['version_name']
  #   version_code = args['version_code']
  #   new_android_release = AndroidRelease(version_name=version_name, version_code=version_code)
  #   g.db.add(new_android_release)
  #   g.db.commit()
  #   return True, 200

class FFmpegController(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('start')
    parser.add_argument('end')
    args = parser.parse_args()
    input_file_path = args['input']
    output_file_path = args['output']
    start = args['start']
    end = args['end']
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
    duration = str(tdelta)
    command = 'ffmpeg -ss "%s" -i "%s" -t "%s" -vcodec copy -acodec copy "%s"' % (start, input_file_path, duration, output_file_path) 
    os.system(command)

    return '', 201

class ThumbnailController(Resource):
  def post(self, media_id):
    media = abort_if_video_doesnt_exist(media_id)
    # return marshal(media, resource_fields), 200
    parser = reqparse.RequestParser()
    parser.add_argument('time')
    args = parser.parse_args()
    if not args['time']:
      return 'No arg time', 400
    screenshot_time = args['time']
    generate_thumbnail(media.uri, media.poster_uri, screenshot_time)
    return '', 200

class MediaList(Resource):
  def post(self):
    # check if the post request has the file part
    if 'file' not in request.files:
      # flash('No file part')
      return 'No file part', 400 
    upload_files = request.files.getlist('file')
    # if user does not select file, browser also
    # submit an empty part without filename
    if not upload_files:
      return 'No selected file', 400
    
    for file in upload_files:
      if file and allowed_file(file.filename):
        f = secure_filename(file.filename)
        # print('f', f)
        path = os.path.join(app.config['UPLOAD_FOLDER'], f)
        file.save(path)

        title, ext = splitext(f)
        if f.lower().endswith(('.mp4', '.jpg', '.jpeg')) and not f.startswith("._"):
          # print('true')
          title = "".join(title)
          # uri = path[len(mypath):]
          root, ext1 = splitext(path)
          poster_uri = "".join(root) + ".jpg"
          
          # An image could be a poster of a video
          # if f.lower().endswith(('.jpg', '.jpeg')) and isfile("".join(root) + ".mp4"):
          #   continue

          # Generate thumbnail if necessary
          if not isfile(poster_uri):
            if ext == ".mp4":
              subprocess.run(
                ["ffmpeg", "-i", path, "-ss", "00:00:01.000", "-vframes", "1", poster_uri],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
              )
                  
          mtimestamp = getmtime(path)
          mdatetime = datetime.fromtimestamp(mtimestamp)
          file_size = getsize(path)

          media_type = get_media_type(f)

          creation_datetime = None
          if media_type == 1:
            meta_data = get_image_metadata(path)
            creation_datetime = meta_data.get('datetime')
          elif media_type == 2:
            creation_datetime = get_datetime(path)
            
          media_datetime = None
          if creation_datetime:
            if media_type == 1:
              media_datetime = datetime.strptime(creation_datetime, '%Y:%m:%d %H:%M:%S')
            elif media_type == 2:
              media_datetime = datetime.strptime(creation_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')
          else:
            media_datetime = mdatetime

          duration = get_duration(path)

          media_dimensions = get_media_dimensions(path, media_type)
          width = media_dimensions.get('width')
          height = media_dimensions.get('height')
            
          v = Media(
            title=title,
            uri=path,
            poster_uri=poster_uri,
            created_at=mdatetime,
            media_type=media_type,
            size=file_size,
            datetime=media_datetime,
            duration=duration,
            filename=f,
            width=width,
            height=height,
          )
          g.db.add(v)
          g.db.commit()
    return '', 201 

api.add_resource(MediaList, '/media')
api.add_resource(ThumbnailController, '/thumbnail/<media_id>')
api.add_resource(FFmpegController, '/ffmpeg')
api.add_resource(MediaController, '/media/<media_id>')
api.add_resource(ShotList, '/shots')
api.add_resource(CastController, '/cast')
api.add_resource(AndroidReleaseController, '/android')
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
