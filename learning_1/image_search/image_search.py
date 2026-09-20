import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader

chromadb_client = chromadb.PersistentClient(path="./db/persistent_storage")
image_loader = ImageLoader()
multimodal_ef = OpenCLIPEmbeddingFunction()

multimodal_db = chromadb_client.get_or_create_collection(name="multimodal_db", embedding_function=multimodal_ef, data_loader=image_loader)

multimodal_db.update(
  ids=["0", "1"],
  uris=["images/tiger.webp", "images/lion.webp"],
  metadatas=[{"image_category": "animals"}, {"image_category": "animals"}]
)

# print(multimodal_db.count())

results = multimodal_db.query(
  query_texts=["lion"],
  n_results=2,
  include=['documents', "uris", "metadatas", "distances", "data"],
  where={"image_category": "animals"}
)

print(results)