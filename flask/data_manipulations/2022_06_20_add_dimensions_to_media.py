import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils import get_media_dimensions
from manage import db, Media

for media in db.session.query(Media).all():
  if media.width and media.height:
    continue
  dimensions = get_media_dimensions(media.uri, media.media_type)
  width = dimensions.get('width')
  height = dimensions.get('height')
  media.width = width
  media.height = height
  db.session.add(media)

db.session.commit()
