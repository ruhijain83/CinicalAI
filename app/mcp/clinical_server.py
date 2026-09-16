import sys

from mcp.server import MCPServer


mcp = MCPServer("ClinicalAI")


@mcp.tool()
def lookup_patient(patient_id: str) -> dict:
    """
    Look up a patient by patient ID.
    """

    print(
        "MCP Tool: Lookup Patient",
        file=sys.stderr
    )

    patients = {
        "12345": {
            "id": "12345",
            "name": "John Smith",
            "age": 67,
            "gender": "Male",
            "allergies": "Penicillin",
            "diagnosis": "Pneumonia",
        }
    }

    patient = patients.get(patient_id)

    if not patient:
        return {
            "error": f"Patient {patient_id} was not found."
        }

    return patient


@mcp.tool()
def get_patient_vitals(patient_id: str):
    """
    Get the latest available vital signs for a patient.
    """

    print(
        "MCP Tool: Get Patient Vitals",
        file=sys.stderr
    )

    vitals = {
        "12345": {
            "patient_id": "12345",
            "temperature_f": 101.2,
            "heart_rate": 102,
            "respiratory_rate": 24,
            "oxygen_saturation": 92,
            "blood_pressure": "138/84"
        },
        "67890": {
            "patient_id": "67890",
            "temperature_f": 98.4,
            "heart_rate": 76,
            "respiratory_rate": 16,
            "oxygen_saturation": 98,
            "blood_pressure": "128/78"
        }
    }

    return vitals.get(
        patient_id,
        {"error": "Patient not found"}
    )


if __name__ == "__main__":
    mcp.run()