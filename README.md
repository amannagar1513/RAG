# RAG FastAPI + Chroma Starter 🚀

This is a **Retrieval-Augmented Generation (RAG)** starter project built with **FastAPI**, **ChromaDB**, and **Google Generative AI (Gemini)**.  
It lets you upload documents, embed them into a vector store (Chroma), and ask questions that are answered using both retrieval and LLMs.

---

## 🌐 Live Demo
👉 [API Docs (Swagger UI)](https://rag-glsp.onrender.com/docs)

---

## ✨ Features
- ⚡ FastAPI backend with auto-generated Swagger UI
- 📚 Document ingestion & embedding using ChromaDB
- 🔎 Semantic search over documents
- 🤖 Answer generation using Google Gemini (`google-generativeai`)
- 🐳 Dockerized for easy deployment
- ☁️ Deployed on [Render](https://render.com/)

---

## 🛠️ Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Google Generative AI](https://ai.google.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [Docker](https://www.docker.com/)

---

## 🚀 Getting Started (Local)

### 1️⃣ Clone Repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd rag-fastapi-chroma-starter
```

### 2️⃣ Create `.env`
Make a `.env` file with your API key:
```env
GOOGLE_API_KEY=your_google_api_key_here
CHROMA_DIR=/app/chroma
METADATA_DB=/app/metadata.db
```

### 3️⃣ Run with Docker
```bash
docker compose up --build
```

App will be available at **http://localhost:8000/docs**

---

## 📦 Deployment

This project is already deployed on **Render**:  
👉 [https://rag-glsp.onrender.com/docs](https://rag-glsp.onrender.com/docs)

To deploy your own:
1. Push repo to GitHub.
2. Create new **Web Service** on [Render](https://render.com/).
3. Select **Docker environment**.
4. Add environment variables (same as `.env`).
5. Deploy 🚀

---

## 🧪 API Usage

- Swagger UI: `/docs`
- Redoc: `/redoc`

Example request (search):
```bash
curl -X POST "https://rag-glsp.onrender.com/search"   -H "Content-Type: application/json"   -d '{"query": "What is RAG?"}'
```

---

## 📂 Project Structure
```
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── rag.py           # RAG logic (embedding, search, answer generation)
│   └── ...
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .env.example
```

---

## 🙌 Acknowledgements
- [FastAPI](https://fastapi.tiangolo.com/)
- [Chroma](https://www.trychroma.com/)
- [Google Generative AI](https://ai.google.dev/)

---
