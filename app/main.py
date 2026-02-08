from fastapi import FastAPI
from app.database.session import engine
from app.database.session import engine
from app.database.base import Base

app = FastAPI(title="AI Interview Backend")

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        return {"db": "connected"}

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)