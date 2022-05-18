import sqlalchemy as sa
from sqlalchemy.orm import relationship

from api.database import Base, engine
from api.models import Stav

kategorie_produkt = sa.Table(
    "kategorie_produkt",
    Base.metadata,
    sa.Column("produkt_id", sa.ForeignKey("produkt.id")),
    sa.Column("kategorie_id", sa.ForeignKey("kategorie.id")),
)

obsah_objednavky = sa.Table(
    "obsah_objednavky",
    Base.metadata,
    sa.Column("objednavka_id", sa.ForeignKey("objednavka.id")),
    sa.Column("produkt_id", sa.ForeignKey("produkt.id")),
    sa.Column("pocet", sa.Integer),
)


class ObjednavkaORM(Base):
    __tablename__ = "objednavka"
    id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    timestamp = ...
    stav = sa.Column("stav", sa.Enum(Stav))
    cena = sa.Column("cena", sa.Float)
    produkty = relationship(
        "ProduktORM", secondary=obsah_objednavky, backref="produkty"
    )


class ProduktORM(Base):
    __tablename__ = "produkt"
    id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    nazev = sa.Column("nazev", sa.String)
    cena = sa.Column("cena", sa.Float)
    skryty = sa.Column("skryty", sa.Boolean, default=False)
    kategorie = relationship("KategorieORM", secondary=kategorie_produkt)


class KategorieORM(Base):
    __tablename__ = "kategorie"
    id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    nazev = sa.Column("nazev", sa.String)
    produkty = relationship("ProduktORM", secondary=kategorie_produkt)


Base.metadata.create_all(engine)
