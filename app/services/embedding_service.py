from openai import OpenAI

from app.config import (
    AI_FOUNDRY_ENDPOINT,
    AI_FOUNDRY_KEY,
    EMBEDDING_MODEL
)

client = OpenAI(
    base_url=AI_FOUNDRY_ENDPOINT,
    api_key=AI_FOUNDRY_KEY,
)

def create_embedding(text: str):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding