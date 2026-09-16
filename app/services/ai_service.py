from app.clients.openai_client import client
from app.prompts.clinical_prompt import SYSTEM_PROMPT
from app.prompts.clinical_prompt import RAG_PROMPT


from app.config import (
    AI_MODEL
)

from app.models.chat_models import ChatResponse


def ask(system_prompt: str, user_prompt: str) -> str:
    """
    Generic AI function.
    Every AI capability uses this.
    """

    response = client.responses.create(
        model=AI_MODEL,
        instructions=system_prompt,
        input=user_prompt
    )

    return response.output_text

def ask_ai(question: str) -> ChatResponse:

    answer = ask(
        SYSTEM_PROMPT,
        question
    )

    return ChatResponse(
        answer=answer
    )


def ask_with_context(
    question: str,
    context: str
):

    user_prompt = f"""
Context:
{context}

Question:
{question}
"""

    return ask(
        RAG_PROMPT,
        user_prompt
    )