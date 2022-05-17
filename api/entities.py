import sqlalchemy as sa
from sqlalchemy.orm import relationship

from api.database import Base

kategorie_produkt = sa.Table(
    "kategorie_produkt",
    Base.metadata,
    sa.Column("produkt_id", sa.ForeignKey("produkt.id")),
    sa.Column("kategorie_id", sa.ForeignKey("kategorie.id")),
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
