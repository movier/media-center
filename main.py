from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response
from models import Video 
from db import SessionLocal

# Utility
def get_video(db_session: Session, video_id: int):
    return db_session.query(Video).filter(Video.id == video_id).first()

# Dependency
def get_db(request: Request):
    return request.state.db

app = FastAPI()

@app.get("/videos/{video_id}")
def read_video(video_id: int, db: Session = Depends(get_db)):
    video = get_video(db, video_id=video_id)
    return video


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
