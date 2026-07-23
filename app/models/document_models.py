from pydantic import BaseModel

class UploadDocumentRequest(BaseModel):
    file_path: str


class UploadDocumentResponse(BaseModel):
    message: str
    chunks_uploaded: int