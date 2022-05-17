from api.database import SessionLocal

from fastapi import FastAPI

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
