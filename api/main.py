from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from api import entities, models
from api.database import SessionLocal

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_home():
    return {"res": {"message": "It works"}}


@app.get("/overview", response_model=List[models.ObjednavkaDB])
def overview(db: Session = Depends(get_db)):
    orders = db.query(entities.ObjednavkaORM).all()
    return {"res": orders}
