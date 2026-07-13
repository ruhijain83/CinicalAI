import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

AI_FOUNDRY_ENDPOINT = os.getenv("AI_FOUNDRY_ENDPOINT")
AI_FOUNDRY_KEY = os.getenv("AI_FOUNDRY_KEY")
AI_MODEL = os.getenv("AI_MODEL")

if not (AI_FOUNDRY_ENDPOINT and AI_FOUNDRY_KEY and AI_MODEL):
    raise RuntimeError("AI Foundry config missing — check app/.env is loaded")