import os
from dotenv import load_dotenv
import chromadb
from google import genai
from chromadb.utils import embedding_functions

load_dotenv()

client = genai.Client()
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
  model_name="all-mpnet-base-v2"
)

chromadb_client = chromadb.PersistentClient(
  path="./db/persistent_store"
)
collection = chromadb_client.get_or_create_collection(
  name="youtube_transcript_collection",
  embedding_function=embedding_function
)

def extract_and_chunk_transcript(file_read_path: str, chunk_size: int = 500):
  chunks = []
  current_chunk = ""

  with open(file_read_path, 'r', encoding="utf-8") as f:
    for item in f:
      if len(current_chunk) + len(item) <= chunk_size:
        current_chunk += " " + item
      else:
        chunks.append(current_chunk)
        current_chunk = item

  if current_chunk:
    chunks.append(current_chunk)

  return chunks

def store_in_chromadb(chunks):
  documents = []
  ids = []

  for idx, chunk in enumerate(chunks):
    documents.append(chunk)
    ids.append(f"id_{idx}")

  collection.upsert(
    documents=documents,
    ids=ids
  )
  print(f"Successfully stored {len(chunks)} transcript chunks into ChromaDB.")

# chunks = extract_and_chunk_transcript("./transcript.txt")
# store_in_chromadb(chunks)

query_text = "How do we deploy a trained model in a real application?"

def search_in_transcript(query: str) -> str:
  results = collection.query(
    query_texts=[query],
    n_results=10
  )

  retrieved_chunks = results["documents"][0]
  context = "\n---\n".join(retrieved_chunks)

  prompt = f"""
  You are an assistant answering questions about a YouTube video.
  Answer the user's question using ONLY the provided transcript snippets.
  If the snippet does not contain the answer, say "The video does not mention this."

  TRANSCRIPT CONTEXT:
  {context}

  USER QUESTION:
  {query}
  """

  response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt
  )

  print(f"User Question: {query}")
  return response.text

print(search_in_transcript(query_text))