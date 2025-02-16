from fastapi import FastAPI, UploadFile, File
from typing import List
from utils.extract import extract_text
from utils.faiss_store import add_to_faiss, retrieve_top_k
from utils.groq_api import query_groq
from models.request_models import QueryRequest

# Initialize FastAPI
app = FastAPI()

@app.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    """Upload documents and store embeddings in FAISS."""
    for file in files:
        text = extract_text(file)
        if text:
            text_chunks = [text[i:i+500] for i in range(0, len(text), 500)]
            add_to_faiss(text_chunks, file.filename)
    return {"message": "Documents processed successfully!"}

@app.post("/query/")
async def query_rag(request: QueryRequest):
    """Retrieve relevant text from FAISS and generate a response using Groq."""
    relevant_texts, relevant_metadata = retrieve_top_k(request.query, k=3)
    context = "\n\n".join(relevant_texts)

    response = query_groq(f"Context: {context}\n\nUser query: {request.query}")

    return {
        "response": response,
        "relevant_chunks": relevant_texts,
        "metadata": relevant_metadata
    }

# Run FastAPI: uvicorn main:app --reload
