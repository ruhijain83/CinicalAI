from app.services.retrieval_service import retrieve

context = retrieve(
    "What are symptoms of pneumonia?"
)

print(context)