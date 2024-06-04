from typing import Any, List, Optional
import logging
from app.config import Config
from llama_index.core import QueryBundle
from llama_index.core.retrievers import BaseRetriever
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from llama_index.core.schema import NodeWithScore
from llama_index.core.vector_stores import VectorStoreQuery
from llama_index.core import Settings

logger = logging.getLogger(__name__)

class ElasticRetriever(BaseRetriever):
    """Retriever over an Elasticsearch vector store."""

    def __init__(
        self,
        vector_store: ElasticsearchStore,
        embed_model: Any,
        query_mode: str = "default",
        similarity_top_k: int = 10,
    ) -> None:
        """Init params."""
        self._vector_store = vector_store
        self._embed_model = embed_model
        self._query_mode = query_mode
        self._similarity_top_k = similarity_top_k
        super().__init__()

    def _retrieve(self, query_bundle: QueryBundle) -> List[NodeWithScore]:
        """Retrieve."""
        query_embedding = self._embed_model.get_query_embedding(query_bundle.query_str)
        vector_store_query = VectorStoreQuery(
            query_embedding=query_embedding,
            similarity_top_k=self._similarity_top_k,
            mode=self._query_mode,
        )
        query_result = self._vector_store.query(vector_store_query)

        nodes_with_scores = []
        for index, node in enumerate(query_result.nodes):
            score: Optional[float] = None
            if query_result.similarities is not None:
                score = query_result.similarities[index]
            nodes_with_scores.append(NodeWithScore(node=node, score=score))

        return nodes_with_scores

def get_elastic_retriever() -> ElasticRetriever:
    try:
        vector_store = ElasticsearchStore(
            index_name="walmart_elastic_items_vector",  # Replace with actual index name
            es_url=Config.ELASTICSEARCH_HOST,
            es_user=Config.ELASTICSEARCH_USER,
            es_password=Config.ELASTICSEARCH_PASSWORD,
            text_field='Description',
            vector_field='embeddings'
        )
        query_mode = "default" 
        similarity_top_k = 10  

        retriever = ElasticRetriever(
            vector_store=vector_store,
            embed_model=Settings.embed_model,
            query_mode=query_mode,
            similarity_top_k=similarity_top_k
        )
        return retriever
    except Exception as e:
        logger.error(f"Error initializing ElasticRetriever: {e}")
        raise RuntimeError("Failed to initialize ElasticRetriever") from e
