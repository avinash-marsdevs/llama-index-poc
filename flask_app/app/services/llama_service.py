from app.services.elasticsearch_service import get_elastic_retriever
from llama_index.core.query_engine import RetrieverQueryEngine

def process_query(query_text):
    retriever = get_elastic_retriever()
    query_engine = RetrieverQueryEngine.from_args(retriever)
    response = query_engine.query(query_text)
    documents=[]
    for node in response.metadata.values():
        document = {key: value for key, value in node.items()}
        documents.append(document)

    return {
        "status": True,
        "message": "Query received successfully.",
        "data": {"response": str(response), "documents": documents}
    }
