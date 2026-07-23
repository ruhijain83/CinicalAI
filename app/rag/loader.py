from pathlib import Path

def load_document(path: str) -> str:

    text = Path(path).read_text(encoding="utf-8")

    return text