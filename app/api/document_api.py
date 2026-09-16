from fastapi import APIRouter
from app.models.document_models import (
    UploadDocumentRequest,
    UploadDocumentResponse
)
from app.rag.ingestion import ingest
from app.rag.pipeline import ask


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.get("/health")
def health():

    return {
        "status": "Document API is working"
    }

@router.post(
    "/upload",
    response_model=UploadDocumentResponse
)

def upload_document(request: UploadDocumentRequest):

    chunks = ingest(
        request.file_path
    )

    return UploadDocumentResponse(
        message="Upload successful",
        chunks_uploaded=chunks
    )