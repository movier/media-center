from sqlalchemy import create_engine
from models import Base, User
from sqlalchemy.orm import sessionmaker

# SQLAlchemy specific code, as with any other app
SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URI = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db_session = SessionLocal()

first_user = db_session.query(User).first()
if not first_user:
    u = User(email="aaaaandoe@example.com", hashed_password="notreallyhashed")
    db_session.add(u)
    db_session.commit()

db_session.close()
