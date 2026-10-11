from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL: set = "mysql+pymysql://root:root@localhost:3306/learning"

engin = create_engine(url=DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engin, autoflush=False)

def get_db():
  db = SessionLocal()
  try:
    yield db
  except:
    db.rollback()
    raise
  finally:
    db.close()

class Base(DeclarativeBase):
  pass