from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with
from database import db_session
from models import Video

app = Flask(__name__)
api = Api(app)

resource_fields = {
  'id': fields.Integer,
  'title': fields.String,
  'uri': fields.String,
  'poster_uri': fields.String
}

class HelloWorld(Resource):
  @marshal_with(resource_fields)
  def get(self):
    return Video.query.all()

api.add_resource(HelloWorld, '/')

@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()
