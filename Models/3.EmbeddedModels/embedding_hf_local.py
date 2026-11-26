from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the capital of india"

docs = [
    "Delhi is the capital of india",
    "Kolkata is the capital of west bengal",
    "Paris is the capital of France"
]

# vector = embedding.embed_query(text)
vector = embedding.embed_documents(docs)

print(str(vector))