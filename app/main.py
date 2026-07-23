from fastapi import FastAPI
from app.models.chat_models import Patient, ChatRequest, ChatResponse
from app.services.user_service import get_user
from app.services.ai_service import ask_ai
from app.api.document_api import router as document_router
from app.api.chat_api import router as chat_router

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Clinical AI Assistant"
    }

@app.get("/patient")
def get_patient() -> Patient:
    return Patient( name = "Ruhi Jain",age = 46, diagnosis ="Fever")

@app.get("/doctor")
def get_doctor() -> dict:
    return {
    "name":"Paul",
    "hospital":"MGH"
    }

@app.post("/patient")
def create_patient(patient: Patient):
    return {
        "message": f"Patient {patient.name} created successfully.",
        "patient": patient
    }

@app.get("/user")
def user():

    return get_user()


app.include_router(document_router)
app.include_router(chat_router)

