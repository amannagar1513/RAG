from typing import List, Dict, Any, Optional
import chromadb
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(context, query):
    model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-pro"
    prompt = f"Answer the question based on the context.\n\nContext:\n{context}\n\nQuestion: {query}\n\nAnswer:"
    response = model.generate_content(prompt)
    return response.text

# -------------------------------
# Embeddings & ChromaDB Setup
# -------------------------------
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
CHROMA_DIR = os.environ.get("CHROMA_DIR", "./chroma")
CHROMA_TELEMETRY_ENABLED = os.environ.get("CHROMA_TELEMETRY_ENABLED", "false").lower() == "true"

# Lazy singletons
_sentence_model: Optional[SentenceTransformer] = None
_client: Optional[chromadb.PersistentClient] = None
_collection = None

def get_sentence_model() -> SentenceTransformer:
    global _sentence_model
    if _sentence_model is None:
        _sentence_model = SentenceTransformer(EMBEDDING_MODEL)
    return _sentence_model

def get_client() -> chromadb.PersistentClient:
    global _client
    if _client is None:
        _client = chromadb.PersistentClient(path=CHROMA_DIR)
    return _client

def get_collection():
    global _collection
    if _collection is None:
        client = get_client()
        _collection = client.get_or_create_collection(name="docs")
    return _collection

# -------------------------------
# Document Management
# -------------------------------
def embed_texts(texts: List[str]) -> List[List[float]]:
    model = get_sentence_model()
    return model.encode(texts, normalize_embeddings=True).tolist()

def add_documents(doc_id: str, chunks: List[str]) -> int:
    """
    Add document chunks to ChromaDB.
    """
    collection = get_collection()
    ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
    embeddings = embed_texts(chunks)
    metadatas = [{"doc_id": doc_id, "chunk_index": i} for i in range(len(chunks))]
    
    collection.add(documents=chunks, embeddings=embeddings, ids=ids, metadatas=metadatas)
    return len(chunks)

def search(query: str, top_k: int = 4) -> List[Dict[str, Any]]:
    """
    Search ChromaDB and return top_k document chunks with metadata.
    """
    collection = get_collection()
    q_emb = embed_texts([query])[0]
    
    # Query ChromaDB
    res = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )
    
    out = []
    for i in range(len(res["documents"][0])):
        out.append({
            "id": res["metadatas"][0][i].get("doc_id", "") + f"_{i}",
            "document": res["documents"][0][i],
            "metadata": res["metadatas"][0][i],
            "distance": res["distances"][0][i],
        })
    return out
