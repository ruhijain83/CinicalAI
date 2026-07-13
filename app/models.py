from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    diagnosis : str

class ChatRequest(BaseModel):
    question : str

class ChatResponse(BaseModel):
    answer : str
    