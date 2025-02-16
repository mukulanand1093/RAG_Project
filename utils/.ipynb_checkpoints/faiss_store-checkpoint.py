#========FAISS Storage & Retrieval==========

import faiss
import numpy as np
from config import D
from utils.embeddings import get_embedding

# Initialize FAISS index
index = faiss.IndexFlatL2(D)
documents = []
metadata = []

def add_to_faiss(text_chunks, filename):
    """Add text chunks & embeddings to FAISS."""
    global documents, metadata

    for i, chunk in enumerate(text_chunks):
        embedding = get_embedding(chunk)
        embedding_np = np.array([embedding], dtype=np.float32)
        index.add(embedding_np)

        documents.append(chunk)
        metadata.append({"filename": filename, "chunk_index": i})

def retrieve_top_k(query: str, k=3):
    """Retrieve the top K relevant text chunks from FAISS."""
    if index.ntotal == 0:
        return [], []

    query_embedding = get_embedding(query)
    query_embedding_np = np.array([query_embedding], dtype=np.float32)

    distances, indices = index.search(query_embedding_np, k)
    retrieved_texts, retrieved_metadata = [], []

    for i in indices[0]:
        if 0 <= i < len(documents):
            retrieved_texts.append(documents[i])
            retrieved_metadata.append(metadata[i])

    return retrieved_texts, retrieved_metadata
