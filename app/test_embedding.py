from app.services.embedding_service import create_embedding
from app.services.vector_service import cosine_similarity

doc1 = "Pneumonia is an infection of the lungs."

doc2 = "Lung infection"

doc3 = "MRI uses magnets."

embedding1 = create_embedding(doc1)

embedding2 = create_embedding(doc2)

embedding3 = create_embedding(doc3)

print(

    cosine_similarity(
        embedding1,
        embedding2
    )
)

print(

    cosine_similarity(
        embedding1,
        embedding3
    )
)