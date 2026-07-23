from app.rag.loader import load_document

text = load_document(
    "data/clinical_guidelines.txt"
)

print(text)