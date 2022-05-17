from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api import config

engine = create_engine(config.DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autflush=False, bind=engine)
Base = declarative_base()
