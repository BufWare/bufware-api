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
    timestamp: int
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
    skryty: bool


class ProduktDB(ProduktBase):
    class Config:
        orm_mode = True

    id: int


class KategorieBase(BaseModel):
    nazev: str


class KategorieDB(KategorieBase):
    class Config:
        orm_mode = True

    id: int
