from pymongo import MongoClient
from pydantic import BaseModel, Field, GetCoreSchemaHandler
from typing import Optional
from bson import ObjectId

client = MongoClient(host="mongodb://root:root@localhost:27017")
db = client["python_learning"]

db.drop_collection(name_or_collection="users")
db.drop_collection(name_or_collection="accounts")

user_collection = db['users']
account_collection = db['accounts']

# Models
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

def create_user_and_account_transaction():
  with client.start_session() as session:
    with session.start_transaction():
      try:
        valid_user_dict = {"name": "Demo", "age": 25, "role": "admin"}
        user = UserModel(**valid_user_dict)
        user_insert_result = user_collection.insert_one(user.model_dump())
        print("User created, ID:", user_insert_result.inserted_id)

        valid_account_data = {"user_id": str(user_insert_result.inserted_id)}
        account = AccountModel(**valid_account_data)
        account_dict = account.model_dump()
        account_dict["user_id"] = ObjectId(account.user_id)
      
        result = account_collection.insert_one(account_dict)
        print(f"Account created. account id: {result.inserted_id}, user_id: {account.user_id}")
      except Exception as e:
        print(f"Transaction aborted due to error: {e}")
        raise e

create_user_and_account_transaction()