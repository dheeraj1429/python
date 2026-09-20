from chromadb.utils import embedding_functions


default_em = embedding_functions.DefaultEmbeddingFunction()

emd = default_em("Any name")
print(emd)