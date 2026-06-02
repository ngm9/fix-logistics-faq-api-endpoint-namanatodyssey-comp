import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
STORAGE_DIR = BASE_DIR / "storage" / "logistics_faq"

CHUNK_SIZE = 512
CHUNK_OVERLAP = 50
TOP_K = 3
