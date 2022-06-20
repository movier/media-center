import os
from manage import db, Media

base_path = "/mnt/sda4/data/kids"
# base_path = "/mnt/sda4/data/AI"

for media in db.session.query(Media).all():
  if os.path.isfile(media.uri):
    file_size = os.path.getsize(media.uri)
    media.size = file_size
    media.media_type = 1
    db.session.add(media)

db.session.commit()
