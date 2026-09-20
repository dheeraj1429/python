from pymongo import MongoClient
client = MongoClient(host="mongodb://root:root@localhost:27017")
db = client["python_learning"]
collection = db['users']

try:
  user = {"name": "Demo user", "age": 10, "role": "admin"}
  collection.delete_many({"name": "Demo user"})
  result = collection.insert_one(user)
  print("Inserted ID:", result.inserted_id)
except Exception as e:
  print(f"Error while inserting using: {e}")


try:
  fetch_user_by_age = collection.aggregate(
    pipeline=[
      {"$match": {"age": {"$gte": 8}}}
    ]
  )
  for doc in fetch_user_by_age:
    print(doc)
except Exception as e:
  print(f"Error while fetching data: {e}")