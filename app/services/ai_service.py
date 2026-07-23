from app.clients.openai_client import client
from app.prompts.clinical_prompt import SYSTEM_PROMPT
from app.prompts.clinical_prompt import RAG_PROMPT


from app.config import (
    AI_MODEL
)

from app.models.chat_models import ChatResponse


def ask_ai(question: str) -> ChatResponse:

    response = client.responses.create(
        model=AI_MODEL,
         instructions=SYSTEM_PROMPT,
        input=question
    )

    return ChatResponse(
        answer=response.output_text
    )


def ask_with_context(question: str, context: str):

   prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )
   
   response = client.responses.create(
        model=AI_MODEL,
        instructions=SYSTEM_PROMPT,
        input=prompt
    )
   
   return response.output_text