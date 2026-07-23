from openai import OpenAI

from app.config import (
    AI_FOUNDRY_ENDPOINT,
    AI_FOUNDRY_KEY,
)

client = OpenAI(
    base_url=AI_FOUNDRY_ENDPOINT,
    api_key=AI_FOUNDRY_KEY,
)