import chromadb
from chromadb.utils import embedding_functions

chromadb_client = chromadb.Client()
default_em = embedding_functions.DefaultEmbeddingFunction()

# Clear cache
# chromadb_client.clear_system_cache()

collection = chromadb_client.get_or_create_collection(name="my_testing_collection", embedding_function=default_em)

# Define text documents
documents = [
    {
        "id": "doc1",
        "text": "Python is a popular programming language used for web development, automation, data analysis, and artificial intelligence."
    },
    {
        "id": "doc2",
        "text": "Machine learning allows computers to learn patterns from data and make predictions without being explicitly programmed for every task."
    },
    {
        "id": "doc3",
        "text": "Deep learning is a subset of machine learning that uses neural networks with multiple layers to learn complex patterns."
    },
    {
        "id": "doc4",
        "text": "React Native is a framework for building mobile applications using JavaScript and React. It allows developers to create applications for both iOS and Android."
    },
    {
        "id": "doc5",
        "text": "Docker is a platform that packages applications and their dependencies into containers so they can run consistently across different environments."
    },
    {
        "id": "doc6",
        "text": "Kubernetes is a container orchestration platform that automates deployment, scaling, and management of containerized applications."
    },
    {
        "id": "doc7",
        "text": "A database is used to store and organize information so that applications can efficiently create, read, update, and delete data."
    },
    {
        "id": "doc8",
        "text": "Vector databases store numerical vector representations of data and are commonly used for semantic search and retrieval augmented generation."
    },
    {
        "id": "doc9",
        "text": "Embeddings convert text, images, or other data into numerical vectors that capture semantic meaning. Similar pieces of content have similar vector representations."
    },
    {
        "id": "doc10",
        "text": "Retrieval augmented generation combines a language model with a retrieval system. Relevant documents are retrieved first and then provided to the language model as context."
    },
]

collection.upsert(
  ids=list(map(lambda elem: elem["id"], documents)),
  documents=list(map(lambda elem: elem["text"], documents))
)

# Define the query
query_text = "How can I make an AI application understand my documents?"

results = collection.query(
  query_texts=[query_text],
  n_results=3
)

print(
  collection.get(
    include=['documents', "embeddings"]
  )
)

for (idx, documents) in enumerate(results["documents"][0]):
  doc_id = results['ids'][0][idx]
  distance = results['distances'][0][idx]
  print(f"For the query '{query_text}', \nFound similar documents: {documents} (ID: {doc_id}, Distance: {distance})")