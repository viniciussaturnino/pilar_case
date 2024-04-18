from enum import Enum
from typing import List
from pydantic import BaseModel


class BaseRequest(BaseModel):
    words: List[str]


class SortOrderEnum(str, Enum):
    ASC = "asc"
    DESC = "desc"


class SortRequest(BaseRequest):
    order: SortOrderEnum
