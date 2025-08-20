import os
from app.chunking import simple_word_chunk

def test_chunking_basic():
    text = " ".join([f"word{i}" for i in range(1200)])
    chunks = simple_word_chunk(text, chunk_size=200, overlap=20)
    assert len(chunks) > 1
    assert any("word0" in c for c in chunks)
