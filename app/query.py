import logging
from typing import Any

from llama_index.core import VectorStoreIndex

from app.config import TOP_K

logger = logging.getLogger(__name__)


def build_query_engine(index: VectorStoreIndex) -> Any:
    query_engine = index.as_query_engine(similarity_top_k=TOP_K)
    return query_engine


def run_query(query_engine: Any, question: str) -> dict:
    response = query_engine.query(question)
    answer = str(response)
    sources = []
    return {"answer": answer, "sources": sources}
