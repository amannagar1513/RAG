# RAG
Retrieval-Augmented Generation (RAG) pipeline built with FastAPI and ChromaDB. Supports document upload, chunking, vector embeddings, and contextual query answering using LLMs (Gemini). Includes REST API endpoints, metadata storage, and workflow automation integration.
# RAG FastAPI + ChromaDB

A Retrieval-Augmented Generation (RAG) pipeline built with **FastAPI**, **ChromaDB**, and **LLM APIs** (OpenAI/Gemini). This project allows users to upload documents, query them using natural language, and receive contextual AI-generated answers. It also supports workflow automation using n8n.

---

## Features

- Upload multiple documents (supports large files with chunking)
- Store document embeddings in **ChromaDB** for efficient retrieval
- Query documents using natural language
- Generate contextual answers using LLMs (OpenAI GPT-4o-mini or Google Gemini)
- Document metadata management
- Dockerized setup for local or cloud deployment
- Optional workflow automation examples using **n8n**

---

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Vector Database:** ChromaDB
- **Embeddings:** SentenceTransformers (`all-MiniLM-L6-v2`)
- **LLM API:** OpenAI GPT-4o-mini / Google Gemini
- **Dev Tools:** Docker, Git, VS Code
- **Optional Automation:** n8n

---

## Installation

### 1. Clone the repository


