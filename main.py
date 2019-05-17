from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response
from models import User
from db import SessionLocal

# Utility
def get_user(db_session: Session, user_id: int):
    return db_session.query(User).filter(User.id == user_id).first()

# Dependency
def get_db(request: Request):
    return request.state.db

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id=user_id)
    return user


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
