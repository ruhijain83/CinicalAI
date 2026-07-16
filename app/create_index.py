from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
)

from app.config import (
    AZURE_SEARCH_ENDPOINT,
    AZURE_SEARCH_KEY,
    SEARCH_INDEX,
)

credential = AzureKeyCredential(AZURE_SEARCH_KEY)

client = SearchIndexClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    credential=credential
)

fields = [

    SimpleField(
        name="id",
        type=SearchFieldDataType.String,
        key=True
    ),

    SearchableField(
        name="title",
        type=SearchFieldDataType.String
    ),

    SearchableField(
        name="content",
        type=SearchFieldDataType.String
    ),

    SearchField(
        name="contentVector",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=1536,
        vector_search_profile_name="vector-profile"
    )
]

vector_search = VectorSearch(

    algorithms=[
        HnswAlgorithmConfiguration(
            name="hnsw-config"
        )
    ],

    profiles=[
        VectorSearchProfile(
            name="vector-profile",
            algorithm_configuration_name="hnsw-config"
        )
    ]
)

index = SearchIndex(
    name=SEARCH_INDEX,
    fields=fields,
    vector_search=vector_search
)

client.create_or_update_index(index)

print(f"Index '{SEARCH_INDEX}' created successfully.")