from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class Stav(Enum):
    OBJEDNANO = 0
    PRIPRAVENO = 1
    VYDANO = 2
    ZRUSENO = 3


class ObjednavkaBase(BaseModel):
    cena: float
    timestamp: datetime
    stav: Stav


class ObjednavkaDB(ObjednavkaBase):
    class Config:
        orm_mode = True

    id: int


class ProduktObsah(BaseModel):
    id: int
    pocet: int


class ObjednavkaData(BaseModel):
    produkty: List[ProduktObsah]


class ProduktBase(BaseModel):
    nazev: str
    cena: float


class ProduktDB(ProduktBase):
    class Config:
        orm_mode = True

    id: int
    skryty: bool


class ProduktData(ProduktBase):
    kategorie: List[int]


class KategorieBase(BaseModel):
    nazev: str


class KategorieDB(KategorieBase):
    class Config:
        orm_mode = True

    id: int


class KategorieData(KategorieBase):
    pass
