from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient

from app.config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
)

credential = AzureKeyCredential(AZURE_SEARCH_KEY)

index_client = SearchIndexClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    credential=credential
)