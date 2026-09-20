from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_qdrant import QdrantVectorStore
from pathlib import Path

pdf_path = Path(__file__).parent / "nodejs.pdf"

# Load this file into the python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# Split the docs into the smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
  chunk_size=1000,
  chunk_overlap=400
)

chunks = text_splitter.split_documents(documents=docs)
# chunks_text = [chunk.page_content for chunk in chunks]

# Embed documents
embeddings = FastEmbedEmbeddings(model_name="BAAI/bge-small-en-v1.5")
# doc_vectors = embeddings.embed_documents(chunks_text)

vector_store = QdrantVectorStore.from_documents(
  documents=chunks,
  embedding=embeddings,
  url="http://localhost:6333",
  collection_name="learning_rag"
)

print("Indexing of documents done...")