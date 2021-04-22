import os
from manage import db, Media

base_path = "/mnt/sda4/data/kids"
# base_path = "/mnt/sda4/data/AI"

for media in db.session.query(Media).all():
  media.uri = base_path + media.uri
  media.poster_uri = base_path + media.poster_uri
  db.session.add(media)

db.session.commit()
