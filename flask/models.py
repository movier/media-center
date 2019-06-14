from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Video(Base):
  __tablename__ = 'videos'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  uri = Column(String)
  poster_uri = Column(String)
  mtime = Column(DateTime, index=True)
