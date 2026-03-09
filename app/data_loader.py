import json
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "products.json"


def load_products() -> List[Dict]:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Products file not found at: {DATA_FILE}")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)