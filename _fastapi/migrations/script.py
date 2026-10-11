from database import Base, engin
from models import user_model

def init_db():
  print("Creating tables in MySQL...")
  Base.metadata.create_all(bind=engin)
  print("Tables created successfully!")

if __name__ == "__main__":
  init_db()