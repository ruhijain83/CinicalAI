from app.agents.tools import (
    search_clinical_guidelines,
    lookup_patient,
    general_chat
)

from app.agents.planner import choose_tool


def run(question: str):

    tool = choose_tool(question)

    print(f"Planner selected: {tool}")

    if tool == "lookup_patient":

        return lookup_patient("12345")

    elif tool == "search_guidelines":

        return search_clinical_guidelines(question)

    else:

        return general_chat(question)