from pymongo import MongoClient
client = MongoClient(host="mongodb://root:root@localhost:27017")
db = client["python_learning"]
user_collection = db['users']
account_collection = db['accounts']

# Referencing document
def insert_user_doc():
  try:
    user_doc = {"name": "Demo", "age": 10, "place": "new delhi"}
    result = user_collection.insert_one(user_doc)
    return result.inserted_id
  except Exception as e:
    print("Error during inserting user document")
    raise e

def insert_account_doc():
  try:
    user_document_id = insert_user_doc()
    account_doc = {"user_id": user_document_id}
    result = account_collection.insert_one(account_doc)
    print(f"Inserted account doc: account id: {result.inserted_id}, user id: {user_document_id}")
  except Exception as e:
    print("Error during inserting account doc")
    raise e

insert_account_doc()