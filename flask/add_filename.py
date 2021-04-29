import os
from manage import db, Media

for media in db.session.query(Media).all():
  media.filename = media.title + '.mp4'
  db.session.add(media)

db.session.commit()
