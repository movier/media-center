from datetime import datetime
from manage import db, Media
from utils import get_image_metadata 

for image in db.session.query(Media).filter(Media.media_type == 1).all():
  meta_data = get_image_metadata(image.uri)
  if not 'DateTime' in meta_data:
    continue
  img_datetime = meta_data['DateTime']
  img_datetime = img_datetime.replace('-', ':')
  img_datetime = datetime.strptime(img_datetime, '%Y:%m:%d %H:%M:%S')
  image.datetime = img_datetime
  db.session.add(image)

db.session.commit()
