from app.rag.loader import load_document
from app.rag.chunker import chunk_text

text = load_document(
    "data/clinical_guidelines.txt"
)

chunks = chunk_text(text)

print(len(chunks))

for i, chunk in enumerate(chunks):

    print()

    print(f"Chunk {i}")

    print(chunk)