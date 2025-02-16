
#=======Embedding Generator========

import torch
import numpy as np
from transformers import AutoModel, AutoTokenizer
from config import EMBEDDING_MODEL

# Load model & tokenizer
tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL)
model = AutoModel.from_pretrained(EMBEDDING_MODEL)

def get_embedding(text: str) -> np.ndarray:
    """Generate embeddings for text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state[:, 0, :].detach().cpu().numpy()
    return embeddings[0].astype(np.float32)
