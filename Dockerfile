# Simple Dockerfile for the FastAPI RAG app
FROM python:3.11-slim

WORKDIR /app

# System deps for sentence-transformers (torch) and pypdf may be heavy.
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV CHROMA_DIR=/app/chroma
ENV METADATA_DB=/app/metadata.db
EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
