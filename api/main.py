from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from api.database import SessionLocal
from api.entities import (KategorieORM, ObjednavkaORM, ObsahObjednavky,
                          ProduktORM)
from api.models import ObjednavkaData, ObjednavkaDB, ProduktData, ProduktDB

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_home():
    return {"message": "Funguju!"}


@app.get("/overview")
def overview(session: Session = Depends(get_db)):
    orders = session.query(ObjednavkaORM).all()
    return orders


@app.post("/product")
def create_product(prod_data: ProduktData, session: Session = Depends(get_db)):

    categories = []
    for kategorie in prod_data.kategorie:
        category = session.query(KategorieORM).get(kategorie)
        if category is not None:
            categories.append(category)

    product = ProduktORM(
        nazev=prod_data.nazev,
        cena=prod_data.cena,
    )
    product.kategorie = categories

    session.add(product)
    session.commit()

    return {"res": ProduktDB.from_orm(product)}


@app.post("/order")
def create_order(obj_data: ObjednavkaData, session: Session = Depends(get_db)):
    cena = 0
    produkty = []
    for produkt in obj_data.data:
        produkt_db = session.query(ProduktORM).get(produkt.id)

        if produkt_db is None:
            return {"error": "Neznámý produkt"}

        produkty.append((produkt_db, produkt.pocet))
        cena += produkt_db.cena * produkt.pocet

    objednavka = ObjednavkaORM(cena=cena)
    session.add(objednavka)
    session.commit()
    for produkt, pocet in produkty:
        obsah = ObsahObjednavky(
            objednavka_id=objednavka.id, produkt_id=produkt.id, pocet=pocet
        )
        session.add(obsah)

    session.commit()
    return {"res": ObjednavkaDB.from_orm(objednavka)}
