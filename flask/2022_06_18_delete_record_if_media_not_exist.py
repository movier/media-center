from manage import db, Media
from os.path import isfile

for media in db.session.query(Media).all():
  if not isfile(media.uri):
    db.session.delete(media)
db.session.commit()
