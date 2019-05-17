from sqlalchemy import create_engine
from models import Base, Video
from sqlalchemy.orm import sessionmaker
from db import engine, SessionLocal

Base.metadata.create_all(bind=engine)

db_session = SessionLocal()

first_video = db_session.query(Video).first()
if not first_video:
    v = Video(title="sample-video", uri="folder/sample-video.mp4", poster_uri="folder/sample-video.jpg")
    db_session.add(v)
    db_session.commit()

db_session.close()
