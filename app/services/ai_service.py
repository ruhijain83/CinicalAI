from openai import OpenAI

from app.config import (
    AI_FOUNDRY_ENDPOINT,
    AI_FOUNDRY_KEY,
    AI_MODEL,
)

from app.models import ChatResponse

client = OpenAI(
    base_url=AI_FOUNDRY_ENDPOINT,
    api_key=AI_FOUNDRY_KEY,
)

def ask_ai(question: str) -> ChatResponse:

    response = client.responses.create(
        model=AI_MODEL,
         instructions="""
            You are an experienced clinical AI assistant.

            Rules:
            - Explain medical terms in simple language.
            - Never invent patient information.
            - If uncertain, say you are uncertain.
            - Do not replace professional medical advice.
            """,
        input=question
    )

    return ChatResponse(
        answer=response.output_text
    )


def ask_with_context(question: str, context: str):

    prompt = f"""
    You are a clinical assistant.

    Use ONLY the information below to answer.

    Context:
    {context}

    Question:
    {question}
    """

    response = client.responses.create(
        model=AI_MODEL,
        input=prompt
    )

    return response.output_text