#=====File Text Extraction======

import pdfplumber
from docx import Document
from fastapi import UploadFile

def extract_text(file: UploadFile) -> str:
    """Extract text from supported document types."""
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "\n".join([page.extract_text() or "" for page in pdf.pages])
    elif file.filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file.filename.endswith(".txt"):
        return file.file.read().decode("utf-8")
    return None
