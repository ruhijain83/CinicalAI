from app.agents.tools import (
    lookup_patient,
    search_clinical_guidelines,
    calculate,
    general_chat
)


TOOL_REGISTRY = {
    "lookup_patient": lookup_patient,
    "search_clinical_guidelines": search_clinical_guidelines,
    "calculate": calculate,
    "general_chat": general_chat
}