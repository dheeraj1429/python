from fastapi import FastAPI, Depends, HTTPException, status
from database import Base, engin, get_db, DbSession
import models
from schema import CreateUser, UserResponse, UpdateUser
from sqlalchemy.orm import Session

app = FastAPI()

@app.delete(
  "/delete-user/{user_id}"
)
async def delete_user(user_id: int, db: DbSession):
  db_user = db.query(models.User).filter(models.User.id == user_id).first()
  if not db_user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"User account not found with id: {user_id}"
    )

  db.delete(db_user)
  db.commit()

  return None

@app.put(
  "/update-user"
)
async def update_user(user: UpdateUser, db: DbSession):
  db_user = db.query(models.User).filter(models.User.id == user.id).first()
  if not db_user:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"User with id {user.id} not found",
    )

  if user.email and db_user.email != user.email:
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_email:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Email already registered",
      )

  update_user = user.model_dump(exclude_unset=True, exclude={"id"})

  for filed, value in update_user.items():
    setattr(db_user, filed, value)

  db.commit()
  db.refresh(db_user)
  return db_user

@app.get(
  "/get-user-by-email/{email}",
  response_model=UserResponse
)
async def get_user_by_email(email: str, db: DbSession):
  db_user = db.query(models.User).filter(models.User.email == email).first()
  if not db_user:
    raise HTTPException(status_code=404, detail="User not found")

  return db_user

@app.post(
  "/create-user",
  status_code=status.HTTP_201_CREATED
)
async def created_user(user: CreateUser, db: DbSession):
  db_user = db.query(models.User).filter(models.User.email == user.email).first()
  if db_user:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail="Email already registered"
    )

  new_user = models.User(
    username=user.username,
    email=user.email,
    bio=user.bio
  )

  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def init_db():
  print("Creating tables in MySQL...")
  Base.metadata.create_all(bind=engin)
  print("Tables created successfully!")

if __name__ == "__main__":
  init_db()