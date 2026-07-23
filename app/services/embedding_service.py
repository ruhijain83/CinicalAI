from app.clients.openai_client import client

from app.config import (
    EMBEDDING_MODEL
)


def create_embedding(text: str) -> list[float]:
    """Generate an embedding for the given text."""
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding