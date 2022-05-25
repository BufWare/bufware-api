from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from api import entities
from api.database import SessionLocal
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
def overview(s: Session = Depends(get_db)):
    orders = s.query(entities.ObjednavkaORM).all()
    return orders


@app.get("/menu")
def get_menu(s: Session = Depends(get_db)):
    products = s.query(entities.ProduktORM).all()
    return products


@app.post("/product")
def create_product(prod_data: ProduktData, s: Session = Depends(get_db)):

    categories = []
    for kategorie in prod_data.kategorie:
        category = s.query(entities.KategorieORM).get(kategorie)
        if category is not None:
            categories.append(category)

    product = entities.ProduktORM(
        nazev=prod_data.nazev,
        cena=prod_data.cena,
    )
    product.kategorie = categories

    s.add(product)
    s.commit()

    return {"res": ProduktDB.from_orm(product)}


@app.post("/order")
def create_order(obj_data: ObjednavkaData, s: Session = Depends(get_db)):
    cena = 0
    produkty = []
    for produkt in obj_data.data:
        produkt_db = s.query(entities.ProduktORM).get(produkt.id)

        if produkt_db is None:
            return {"error": "Neznámý produkt"}

        produkty.append((produkt_db, produkt.pocet))
        cena += produkt_db.cena * produkt.pocet

    objednavka = entities.ObjednavkaORM(cena=cena)
    s.add(objednavka)
    s.commit()
    for produkt, pocet in produkty:
        obsah = entities.ObsahObjednavky(
            objednavka_id=objednavka.id, produkt_id=produkt.id, pocet=pocet
        )
        s.add(obsah)

    s.commit()
    return {"res": ObjednavkaDB.from_orm(objednavka)}
