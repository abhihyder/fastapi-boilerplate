from pydantic import BaseModel
from typing import List, Optional

class HashtagResponse(BaseModel):
    text: str