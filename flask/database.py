from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:////mnt/sda4/jffs/my-video-app/flask/test.db', convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# engine2 = create_engine('sqlite:////mnt/sda4/jffs/my-video-app/flask/kids.db', convert_unicode=True)
# db_session2 = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine2))
# Base = declarative_base()
# Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine2)