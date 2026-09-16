from app.services.retrieval_service import retrieve
from app.services.ai_service import ask_ai


def search_clinical_guidelines(question: str):
    """
    Search the clinical knowledge base using RAG.
    """

    print("🔧 Tool: Search Clinical Guidelines")

    context = retrieve(question)

    return context


def lookup_patient(patient_id: str):
    """
    Mock patient lookup.
    Later this will call a real database or API.
    """

    print("🔧 Tool: Lookup Patient")

    patients = {
        "12345": {
            "id": "12345",
            "name": "John Smith",
            "age": 67,
            "gender": "Male",
            "allergies": "Penicillin",
            "diagnosis": "Pneumonia"
        },
        "67890": {
            "id": "67890",
            "name": "Jane Doe",
            "age": 45,
            "gender": "Female",
            "allergies": "None",
            "diagnosis": "Hypertension"
        }
    }

    return patients.get(
        patient_id,
        {"error": "Patient not found"}
    )


def calculate(expression: str):
    """
    Simple calculator tool.
    """

    print("🔧 Tool: Calculator")

    try:
        return str(eval(expression))
    except Exception:
        return "Invalid expression"


def general_chat(question: str):
    """
    General GPT chat.
    """

    print("🔧 Tool: General Chat")

    response = ask_ai(question)

    return response.answer