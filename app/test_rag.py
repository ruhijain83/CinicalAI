from app.knowledge_base import DOCUMENTS
from app.services.vector_service import search
from app.services.ai_service import ask_with_context

question = "Tell me about lung infections."

document, score = search(question, DOCUMENTS)

answer = ask_with_context(
    question,
    document
)

print("Retrieved Document:")
print(document)

print()

print("AI Answer:")
print(answer)