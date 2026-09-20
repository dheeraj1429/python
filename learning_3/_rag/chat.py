import os
from dotenv import load_dotenv
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv("GEMINI_API_KEY"),
  base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")

vector_db = QdrantVectorStore.from_existing_collection(
  collection_name="learning_rag",
  embedding=embeddings,
  url="http://localhost:6333"
)

# Take user input
user_input = input("Ask something... ")

# Relevant chunks from the vector db
search_results = vector_db.similarity_search(query=user_input)

context = "".join([f"Page Content: {results.page_content}\nPage Number: {results.metadata["page_label"]}\nFile Location: {results.metadata["source"]}" for results in search_results])

SYSTEM_PROMPT = """
You are a helpful AI Assistant who answers user query based on the available context retrieved from a PDF file along with page_contents and page number.

You should only answers the user based on the following context and navigate the user to open the right page number to know more.

Context:
{context}
"""

messages = [
  {"role": "system", "content": SYSTEM_PROMPT},
  {"role": "user","content": user_input},
]

response = client.chat.completions.create(
  model="gemini-3.1-flash-lite",
  messages=messages)

print(f"🧠 {response.choices[0].message.content}")