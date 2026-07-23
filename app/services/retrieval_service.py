from app.services.embedding_service import create_embedding
from app.services.search_service import search_documents

def retrieve(question: str):

    question_embedding = create_embedding(question)

    results = search_documents(question_embedding)
    context = "\n\n".join(
    result["content"]
    for result in results
)

    return context