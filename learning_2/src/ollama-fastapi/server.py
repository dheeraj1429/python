from fastapi import FastAPI, Body
from ollama import Client
from pydantic import BaseModel

app = FastAPI()
client = Client(
  host="http://localhost:11434"
)

@app.get("/")
def read_root():
  return {"Hello": "World"}

class Item(BaseModel):
  message: str

@app.post("/chat")
def chat(item: Item):
  response = client.chat(model="gemma:2b", messages=[
    {"role": "user", "content": item.message}
  ])
  return response.message.content