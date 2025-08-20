from typing import List

def simple_word_chunk(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Chunk text roughly by words. chunk_size ~ tokens; overlap to preserve context."""
    words = text.split()
    if not words:
        return []
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        if end == len(words):
            break
        start = max(0, end - overlap)
    return chunks
