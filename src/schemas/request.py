from typing import List
from pydantic import BaseModel


class BaseRequest(BaseModel):
    words: List[str]
