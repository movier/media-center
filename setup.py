from sqlalchemy import create_engine
from models import Base, Video
from sqlalchemy.orm import sessionmaker
from db import engine, SessionLocal
from os import listdir
from os.path import isfile, join, splitext

Base.metadata.create_all(bind=engine)

db_session = SessionLocal()

mypath = "/usr/src/app"

def traverse_dir(base_path):
    for f in listdir(base_path):
        path = join(base_path, f)
        if isfile(path):
            title, ext = splitext(f)
            if ext == ".py":
                title = "".join(title)
                uri = path[len(mypath):]
                root, ext1 = splitext(uri)
                poster_uri = "".join(root) + ".jpg"
                v = Video(title=title, uri=uri, poster_uri=poster_uri)
                db_session.add(v)
        else:
            traverse_dir(path)

traverse_dir(mypath)
db_session.commit()

db_session.close()
