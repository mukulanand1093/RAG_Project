### RAG Project
# RAG Pipeline with FastAPI, FAISS & Groq API

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG) pipeline** that enables users to:
1. **Upload multiple documents (PDF, DOCX, TXT)**
2. **Store document embeddings in FAISS** (for fast retrieval)
3. **Retrieve relevant text chunks based on user queries**
4. **Generate responses using the Groq API**

---

## 📂 Project Structure

```
rag_project/
│── main.py                  # FastAPI application entry point
│── config.py                # Configuration settings (API keys, model names)
│── utils/  
│   │── extract.py           # File extraction functions (PDF, DOCX, TXT)  
│   │── embeddings.py        # Hugging Face embedding generation  
│   │── faiss_store.py       # FAISS index handling (store & retrieve)  
│   │── groq_api.py          # Functions to interact with Groq API  
│── models/  
│   │── request_models.py    # Pydantic request models  
│── requirements.txt         # Dependencies  
│── README.md                # Project Documentation  
```

---

## ⚙️ Installation & Setup

### 🔹 Prerequisites
Ensure you have **Python 3.8+** installed.

### 🔹 Install Dependencies
Run the following command in the project directory:
```bash
pip install -r requirements.txt
```

### 🔹 Set Environment Variables
Before running the project, set the **Groq API key**:
```bash
export GROQ_API_KEY="your-api-key"
```
For Windows (PowerShell):  
```powershell
$env:GROQ_API_KEY="your-api-key"
```

---

## 🚀 Running the Application
Start the FastAPI server using:
```bash
uvicorn main:app --reload
```
This will start the server on `http://127.0.0.1:8000`.

---

## 📤 Uploading Documents

### 🔹 API Endpoint
**`POST /upload/`**  
Uploads and processes one or more documents.

### 🔹 Request Example (Using `curl`)
```bash
curl -X 'POST' 'http://127.0.0.1:8000/upload/' \
  -F 'files=@document.pdf' \
  -F 'files=@notes.docx'
```

### 🔹 Response Example
```json
{
  "message": "Documents processed successfully!"
}
```

---

## 🔍 Querying the RAG System

### 🔹 API Endpoint
**`POST /query/`**  
Retrieves the most relevant document chunks and generates a response.

### 🔹 Request Example
```bash
curl -X 'POST' 'http://127.0.0.1:8000/query/' \
  -H 'Content-Type: application/json' \
  -d '{"query": "What is the main topic of the document?"}'
```

### 🔹 Response Example
```json
{
  "response": "The document discusses AI advancements.",
  "relevant_chunks": [
    "Artificial Intelligence has made significant progress in the last decade..."
  ],
  "metadata": [
    {
      "filename": "document.pdf",
      "chunk_index": 0
    }
  ]
}
```

---

## 🛠️ How It Works

### 1️⃣ Document Upload & Processing
- Extracts text from uploaded files (`extract.py`)
- Splits text into **chunks** (500 characters each)
- Generates **embeddings** using `sentence-transformers/all-MiniLM-L6-v2` (`embeddings.py`)
- Stores embeddings & metadata in **FAISS** (`faiss_store.py`)

### 2️⃣ Querying for Information
- Converts user **query** into an embedding
- Retrieves **top K relevant chunks** from FAISS (`retrieve_top_k`)
- Constructs **context** using retrieved chunks
- Sends **query & context** to the **Groq API** (`groq_api.py`)
- Returns the **AI-generated response**

---

## 🔧 Future Improvements
✅ **Add Support for More File Formats (CSV, HTML, Markdown, etc.)**  
✅ **Use a More Advanced Embedding Model (e.g., BGE or Instructor)**  
✅ **Implement a Persistent FAISS Database (Using SQLite/Redis)**  
✅ **Improve Query Processing (Re-Ranking, Hybrid Search)**  
✅ **Add Authentication & User Management**  

---

## 📬 Contact
For questions or contributions, reach out at: **mukul.anand1093@gmail.com** 🚀

