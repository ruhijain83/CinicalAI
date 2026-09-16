TOOLS = [

    {
        "type": "function",
        "name": "lookup_patient",
        "description": "Look up patient information using a patient ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "patient_id": {
                    "type": "string",
                    "description": "The unique patient ID."
                }
            },
            "required": ["patient_id"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "search_clinical_guidelines",
        "description": "Search the clinical knowledge base for information relevant to a clinical question or diagnosis.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The clinical question, diagnosis, or medical topic to search for."
                }
            },
            "required": ["question"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "calculate",
        "description": "Perform a mathematical calculation.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to calculate."
                }
            },
            "required": ["expression"],
            "additionalProperties": False
        },
        "strict": True
    },

    {
        "type": "function",
        "name": "general_chat",
        "description": "Answer a general question when no specialized clinical tool is required.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The user's general question."
                }
            },
            "required": ["question"],
            "additionalProperties": False
        },
        "strict": True
    }

]