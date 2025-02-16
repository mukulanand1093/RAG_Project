
#====Configuration Settings=====

import os

# ==== API Keys ====
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("❌ Error: GROQ_API_KEY is not set.")

# ==== API URL ====
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# ==== Embedding Model ====
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==== FAISS Settings ====
D = 384  # Embedding dimension
