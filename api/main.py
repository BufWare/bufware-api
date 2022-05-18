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
def get_home(test: models.ProduktBase):
    return {"res": "It works"}


@app.get("/overview")
def overview(db: Session = Depends(get_db)) -> List[models.ObjednavkaDB]:
    orders = db.query(entities.ObjednavkaORM).all()
    return {"res": [map(lambda o: models.ObjednavkaDB.from_orm(o), orders)]}
