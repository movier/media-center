from manage import db, Media
from utils import get_media_type

for media in db.session.query(Media).all():
  media_type = get_media_type(media.uri)
  media.media_type = media_type
  db.session.add(media)

db.session.commit()
