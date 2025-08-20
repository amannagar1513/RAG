import os
import uuid
from typing import List, Tuple

from pypdf import PdfReader

from .chunking import simple_word_chunk

def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    texts = []
    for page in reader.pages:
        try:
            texts.append(page.extract_text() or "")
        except Exception:
            texts.append("")
    return "\n".join(texts)

def extract_text(file_path: str) -> Tuple[str, str]:
    """Return (doc_id, text). Currently supports PDF and TXT."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    else:
        raise ValueError(f"Unsupported file type: {ext}. Use PDF or TXT for this starter.")
    doc_id = str(uuid.uuid4())
    return doc_id, text

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    return simple_word_chunk(text, chunk_size=chunk_size, overlap=overlap)
