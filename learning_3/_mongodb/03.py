from pymongo import MongoClient
from pydantic import BaseModel, Field, GetCoreSchemaHandler
from pydantic_core import core_schema
from typing import Optional, Any
from bson import ObjectId

client = MongoClient(host="mongodb://root:root@localhost:27017")
db = client["python_learning"]

db.drop_collection(name_or_collection="users")
db.drop_collection(name_or_collection="accounts")

user_collection = db['users']
account_collection = db['accounts']

class UserModel(BaseModel):
  name: str
  age: int = Field(
    ...,
    ge=0,
    le=120
  )
  role: str
  place: Optional[str] = None

class AccountModel(BaseModel):
  user_id: str

def insert_user(data: dict) -> str:
  user = UserModel(**data)
  result = user_collection.insert_one(user.model_dump())
  print(f"User created. user id: {result.inserted_id}")
  return str(result.inserted_id)

def insert_account(data: dict):
  account = AccountModel(**data)
  account_dict = account.model_dump()
  account_dict["user_id"] = ObjectId(account.user_id)

  result = account_collection.insert_one(account_dict)
  print(f"Account created. account id: {result.inserted_id}, user_id: {account.user_id}")

try:
    valid_data = {"name": "Demo", "age": 25, "role": "admin"}
    user_id = insert_user(valid_data)
    print("User created, ID:", user_id)
    valid_account_data = {"user_id": user_id}
    insert_account(valid_account_data)
except Exception as e:
    print("Validation failed:", e)

