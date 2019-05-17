from sqlalchemy import create_engine
from models import Base, User
from sqlalchemy.orm import sessionmaker
from db import engine, SessionLocal

Base.metadata.create_all(bind=engine)

db_session = SessionLocal()

first_user = db_session.query(User).first()
if not first_user:
    u = User(email="bbbbbbb@example.com", hashed_password="notreallyhashed")
    db_session.add(u)
    db_session.commit()

db_session.close()
