from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.orm import Session

from api.database import SessionLocal
from api.entities import ObjednavkaORM, ProduktORM
from api.models import ObjednavkaData

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_home():
    return {"message": "It works"}


@app.get("/overview")
def overview(session: Session = Depends(get_db)):
    orders = session.query(ObjednavkaORM).all()
    return orders


@app.post("/order")
def create_order(
    data: ObjednavkaData, res: Response, session: Session = Depends(get_db)
):

    cena = 0
    produkty = []
    for produkt in data.produkty:
        produkt_db = session.query(ProduktORM).get(produkt.id)
        if produkt_db is None:
            res.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Neznámý produkt"}
        produkty.append(produkt_db)
        cena += produkt_db.cena * produkt.pocet

    objednavka = ObjednavkaORM(cena=cena)
    objednavka.produkty = produkty

    session.add(objednavka)
    session.commit()

    return {"res": {"id": objednavka.id, "price": cena}}
