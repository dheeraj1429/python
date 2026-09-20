import chromadb
import json
from chromadb.utils import embedding_functions

# sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2") // default model
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
# default_emb = embedding_functions.DefaultEmbeddingFunction()

with open("./product.json", 'r', encoding='utf-8') as file:
  data = json.load(file)

chromadb_client = chromadb.PersistentClient("./db/chroma_persist")

collection = chromadb_client.get_or_create_collection(name="my_product_collection", embedding_function=sentence_transformer_ef)

collection.upsert(
  ids=list(map(lambda elem: elem["id"], data)),
  documents=list(map(lambda elem: elem["text_to_embed"], data))
)

results = collection.query(
  query_texts=["A wire"],
  n_results=3
)

# print(
#   collection.get(
#     where_document={
#       "$regex": r"\b\d+-.+?\b"
#     }
#   )
# )

print(results)