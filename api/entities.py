from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship

from api.database import Base
from api.models import Stav

kategorie_produkt = sa.Table(
    "kategorie_produkt",
    Base.metadata,
    sa.Column("produkt_id", sa.ForeignKey("produkt.id"), primary_key=True),
    sa.Column("kategorie_id", sa.ForeignKey("kategorie.id"), primary_key=True),
)


class ObsahObjednavky(Base):
    __tablename__ = "obsah_objednavky"
    objednavka_id = sa.Column(
        "objednavka_id", sa.ForeignKey("objednavka.id"), primary_key=True
    )
    produkt_id = sa.Column(
        "produkt_id",
        sa.ForeignKey("produkt.id"),
        primary_key=True,
    )
    pocet = sa.Column("pocet", sa.Integer)
    objednavka = relationship("ObjednavkaORM", back_populates="produkty")
    produkt = relationship("ProduktORM", lazy="subquery")


class ObjednavkaORM(Base):
    __tablename__ = "objednavka"
    id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    timestamp = sa.Column("timestamp", sa.TIMESTAMP, default=datetime.now())
    stav = sa.Column("stav", sa.Enum(Stav), default=Stav.OBJEDNANO)
    cena = sa.Column("cena", sa.Float)
    produkty = relationship(
        "ObsahObjednavky", back_populates="objednavka", lazy="subquery"
    )


class ProduktORM(Base):
    __tablename__ = "produkt"
    id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    nazev = sa.Column("nazev", sa.String)
    cena = sa.Column("cena", sa.Float)
    popis = sa.Column("popis", sa.String)
    skryty = sa.Column("skryty", sa.Boolean, default=False)
    kategorie = relationship(
        "KategorieORM",
        secondary="kategorie_produkt",
        back_populates="produkty",
        lazy="subquery",
    )


class KategorieORM(Base):
    __tablename__ = "kategorie"
    id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    nazev = sa.Column("nazev", sa.String)
    produkty = relationship(
        "ProduktORM",
        secondary="kategorie_produkt",
        back_populates="kategorie",
        lazy="subquery",
    )
