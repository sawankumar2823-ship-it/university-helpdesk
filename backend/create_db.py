import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

documents = []

# Load PDFs
for file in os.listdir("documents"):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(f"documents/{file}")
        documents.extend(loader.load())

# Split text
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

docs = splitter.split_documents(documents)

# Embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create vector DB
vectorstore = FAISS.from_documents(docs, embeddings)

# Save locally
vectorstore.save_local("vectorstore")

print("Vectorstore created successfully!")
