from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with
from database import db_session
from models import Video
from flask_cors import CORS

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

class HelloWorld(Resource):
  @marshal_with(resource_fields)
  def get(self):
    return Video.query.all()

api.add_resource(HelloWorld, '/')

@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()
