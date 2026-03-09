from pydantic import BaseModel
from typing import List


class OutfitRequest(BaseModel):
    items: List[str]