from api import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(config.DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autflush=False, bind=engine)
Base = declarative_base()

