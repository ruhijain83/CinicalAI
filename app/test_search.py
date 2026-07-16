from app.knowledge_base import DOCUMENTS
from app.services.vector_service import search

question = "What is a lung infection?"

document, score = search(question, DOCUMENTS)

print("Question:")
print(question)

print()

print("Best Match:")
print(document)

print()

print(f"Similarity Score: {score:.3f}")