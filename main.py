from fastapi import FastAPI, UploadFile, File
from typing import List
import shutil
import os
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer
import pinecone

app = FastAPI()

UPLOAD_DIR = "uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize Pinecone
pinecone.init(api_key="your-pinecone-api-key")
index = pinecone.Index("semantic-search")

# Load the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def pdf_to_text(file_path):
    return extract_text(file_path)

def get_embedding(text):
    return model.encode(text)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = pdf_to_text(file_location)
    embedding = get_embedding(text)
    index.upsert([(file.filename, embedding)])
    return {"info": f"file '{file.filename}' saved and processed"}

@app.get("/docs")
async def search_docs(q: str):
    query_embedding = get_embedding(q)
    results = index.query(query_embedding, top_k=5)
    return {"query": q, "results": [result['id'] for result in results['matches']]}
