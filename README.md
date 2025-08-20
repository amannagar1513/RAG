# RAG FastAPI + Chroma Starter
LIVE WORKING URL - https://7d089ae3d34d.ngrok-free.app/docs    PLEASE CHECK ***
A minimal Retrieval-Augmented Generation (RAG) pipeline you can run locally or in Docker. Upload PDFs/TXT, embed chunks in ChromaDB, retrieve relevant context, and (optionally) generate an answer using OpenAI. If you don't set an OpenAI key, the API returns the best matching context as a fallback.

## Features
- Upload up to 20 docs (starter supports PDF/TXT).
- Chunking with overlap for better retrieval.
- SentenceTransformer embeddings (default: `all-MiniLM-L6-v2`).
- ChromaDB persistent store.
- Endpoints: `/upload`, `/query`, `/metadata`, `/health`.
- Docker + docker-compose.
- Simple tests.

## Quick Start (Local)
1. **Python 3.11+** recommended.
2. Create & activate venv (optional).
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` (or copy `.env.example`) and set values.
   - If you have an OpenAI key, add `OPENAI_API_KEY=...`.
5. Run API:
   ```bash
   uvicorn app.main:app --reload
   ```
6. Open docs: http://127.0.0.1:8000/docs

### Endpoints
- `POST /upload` (multipart/form-data): Upload a PDF/TXT.
- `POST /query` (application/json):
  ```json
  { "query": "What is this document about?", "top_k": 4 }
  ```
- `GET /metadata`: List uploaded docs.
- `GET /health`: Health check.

## Docker
Build and run:
```bash
docker compose up --build
```
API will be on `http://localhost:8000`.

## Tests
```bash
pytest -q
```

## Notes
- This starter uses local `sentence-transformers` embeddings by default; the first run will download the model.
- For bigger deployments, swap Chroma for a managed vector DB and add auth, rate limits, and better chunking/tokenization.
