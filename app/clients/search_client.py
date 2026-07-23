from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

from app.config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    SEARCH_INDEX,
)

client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY),
)