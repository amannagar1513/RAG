import os
import shutil
from typing import Optional
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

from .rag import add_documents, search, generate_answer
from .ingest import extract_text, chunk_text
from .storage import init_db, insert_document, list_documents
from fastapi import Body

app = FastAPI(title="RAG + Gemini FastAPI", version="0.1.0")

TOP_K = int(os.environ.get("TOP_K", "4"))
MAX_CONTEXT_CHARS = int(os.environ.get("MAX_CONTEXT_CHARS", "5000"))

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI with Gemini is working!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    tmp_dir = "./_tmp"
    os.makedirs(tmp_dir, exist_ok=True)
    tmp_path = os.path.join(tmp_dir, file.filename)
    with open(tmp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    try:
        doc_id, text = extract_text(tmp_path)
        if not text.strip():
            raise HTTPException(status_code=400, detail="Empty text extracted from document.")

        chunks = chunk_text(text, chunk_size=500, overlap=50)
        if not chunks:
            raise HTTPException(status_code=400, detail="Failed to create chunks from document.")

        num = add_documents(doc_id, chunks)
        insert_document(doc_id, file.filename, num)
        return {"doc_id": doc_id, "filename": file.filename, "num_chunks": num}
    finally:
        try:
            os.remove(tmp_path)
        except Exception:
            pass

class QueryRequest(BaseModel):
    query: str = Body(..., max_length=50000)  # Increase as needed
    top_k: Optional[int] = None

@app.post("/query")
def query(req: QueryRequest):
    topk = req.top_k or TOP_K
    hits = search(req.query, top_k=topk)

    context = "\n\n".join([h["document"] for h in hits])
    context = context[:MAX_CONTEXT_CHARS]

    answer = generate_answer(context, req.query)  # Gemini call

    return JSONResponse({
        "answer": answer,
        "matches": [
            {"id": h["id"], "doc_id": h["metadata"]["doc_id"], "distance": h["distance"]}
            for h in hits
        ]
    })

@app.get("/metadata")
def metadata():
    return {"documents": list_documents()}
