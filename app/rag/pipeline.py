from app.services.retrieval_service import retrieve
from app.services.ai_service import ask_with_context

def ask(question: str):

    context = retrieve(question)

    answer = ask_with_context(
        question,
        context
    )

    return answer