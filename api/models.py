from enum import Enum

from pydantic import BaseModel


class Stav(Enum):
    OBJEDNANO = 0
    PRIPRAVENO = 1
    VYDANO = 2
    ZRUSENO = 3


class Objednavka(BaseModel):
    class Config:
        orm_mode = True

    id: int
    cena: float
    timestamp: int
    stav: Stav


class Produkt(BaseModel):
    class Config:
        orm_mode = True

    id: int
    nazev: str
    cena: float
    skryty: bool


class Kategorie(BaseModel):
    class Config:
        orm_mode = True

    id: int
    nazev: str
