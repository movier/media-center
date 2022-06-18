from manage import db, Media
from sqlalchemy import desc
from utils import generate_poster_for_video

for video in db.session.query(Media).filter(Media.media_type == 2).order_by(desc(Media.created_at)).limit(3).all():
  generate_poster_for_video(video)
