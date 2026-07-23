from app.rag.loader import load_document
from app.rag.chunker import chunk_text
from app.services.embedding_service import create_embedding
from app.services.search_service import upload_documents


def prepare_chunks(path: str):

    text = load_document(path)

    chunks = chunk_text(text)

    return chunks

def create_documents(chunks):

    documents = []

    for index, chunk in enumerate(chunks):

        embedding = create_embedding(chunk)

        documents.append({
            "id": str(index),
            "title": f"Chunk {index}",
            "content": chunk,
            "contentVector": embedding
        })

    return documents

def ingest(path: str):

    chunks = prepare_chunks(path)

    documents = create_documents(chunks)

    upload_documents(documents)

    return len(documents)