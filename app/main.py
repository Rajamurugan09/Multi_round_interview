from fastapi import FastAPI
from app.database.session import engine

app = FastAPI(title="AI Interview Backend")

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/db-check")
def db_check():
    with engine.connect() as connection:
        return {"db": "connected"}
