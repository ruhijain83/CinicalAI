import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

AI_FOUNDRY_ENDPOINT = os.getenv("AI_FOUNDRY_ENDPOINT")
AI_FOUNDRY_KEY = os.getenv("AI_FOUNDRY_KEY")
AI_MODEL = os.getenv("AI_MODEL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
SEARCH_INDEX = os.getenv("SEARCH_INDEX")
if not (AI_FOUNDRY_ENDPOINT and AI_FOUNDRY_KEY and AI_MODEL):
    raise RuntimeError("AI Foundry config missing — check app/.env is loaded")