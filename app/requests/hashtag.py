from pydantic import BaseModel
from typing import List, Optional

class HashtagRequest(BaseModel):
    hashtag: str
