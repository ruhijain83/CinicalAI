from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.models import VectorizedQuery
from app.clients.search_client import client


from app.config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
)

credential = AzureKeyCredential(AZURE_SEARCH_KEY)

index_client = SearchIndexClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    credential=credential
)

def upload_documents(documents):

    result = client.upload_documents(documents)

    return result

def search_documents(question_embedding):
    vector_query = VectorizedQuery(
                    vector=question_embedding,
                    k_nearest_neighbors=3,
                    fields="contentVector"
    )

    results = client.search(
        search_text=None,
        vector_queries = [vector_query]
    )

    return list(results)