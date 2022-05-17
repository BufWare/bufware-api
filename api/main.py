from fastapi import FastAPI

from api.database import SessionLocal

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def get_home():
    return {"res": "It works"}
