from fastapi import Depends
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

DATABASE_URL: set = "mysql+pymysql://root:root@localhost:3306/learning"

engin = create_engine(url=DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engin, autoflush=False)

# Define the Base class that all models will inherit from
class Base(DeclarativeBase):
  pass

def get_db():
  db = SessionLocal()
  try:
    yield db
  except:
    db.rollback()
    raise
  finally:
    db.close()

DbSession = Annotated[Session, Depends(get_db)]