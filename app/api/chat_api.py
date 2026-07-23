from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse
from app.rag.pipeline import ask

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer = ask(request.question)

    return ChatResponse(answer=answer)