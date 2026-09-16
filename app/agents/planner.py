from app.services.ai_service import ask

PLANNER_PROMPT = """
You are an AI planner.

Available tools:

1. search_guidelines
2. lookup_patient
3. calculator
4. general_chat

Return ONLY the tool name.
"""


def choose_tool(question):

    tool = ask(
        PLANNER_PROMPT,
        question
    )

    return tool.strip()