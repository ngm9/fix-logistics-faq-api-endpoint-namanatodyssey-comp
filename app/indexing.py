import logging
from pathlib import Path

from llama_index.core import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.node_parser import SentenceSplitter

from app.config import CHUNK_OVERLAP, CHUNK_SIZE, DATA_DIR, STORAGE_DIR

logger = logging.getLogger(__name__)


def load_or_create_index() -> VectorStoreIndex:
    if STORAGE_DIR.exists():
        logger.info("Reloading index from %s", STORAGE_DIR)
        storage_context = StorageContext.from_defaults(persist_dir=str(STORAGE_DIR))
        index = load_index_from_storage(storage_context)
        return index

    logger.info("Building new index from documents in %s", DATA_DIR)
    documents = SimpleDirectoryReader(
        input_dir=str(DATA_DIR),
        filename_as_id=True,
    ).load_data()

    splitter = SentenceSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    index = VectorStoreIndex.from_documents(
        documents,
        transformations=[splitter],
    )

    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    index.storage_context.persist(persist_dir=str(STORAGE_DIR))
    logger.info("Index persisted to %s", STORAGE_DIR)

    return index
