import numpy as np
from app.services.embedding_service import create_embedding

def search(question: str, documents: list[str]):

    question_embedding = create_embedding(question)

    best_document = None
    best_score = -1

    for document in documents:

        document_embedding = create_embedding(document)

        score = cosine_similarity(
            question_embedding,
            document_embedding
        )

        if score > best_score:
            best_score = score
            best_document = document

    return best_document, best_score

def cosine_similarity(vector1, vector2):
    vector1 = np.array(vector1)
    vector2 = np.array(vector2)

    similarity = np.dot(vector1, vector2) / (
        np.linalg.norm(vector1) *
        np.linalg.norm(vector2)
    )

    return similarity