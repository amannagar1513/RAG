import os
import sqlite3
from typing import Dict, Any, List
from datetime import datetime

DB_PATH = os.environ.get("METADATA_DB", "./metadata.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS documents(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_id TEXT,
            filename TEXT,
            num_chunks INTEGER,
            created_at TEXT
        )"""
    )
    conn.commit()
    conn.close()

def insert_document(doc_id: str, filename: str, num_chunks: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO documents(doc_id, filename, num_chunks, created_at) VALUES (?, ?, ?, ?)",
        (doc_id, filename, num_chunks, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()

def list_documents() -> List[Dict[str, Any]]:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT doc_id, filename, num_chunks, created_at FROM documents ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return [
        {"doc_id": r[0], "filename": r[1], "num_chunks": r[2], "created_at": r[3]}
        for r in rows
    ]
